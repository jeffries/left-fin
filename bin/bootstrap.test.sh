#!/bin/bash

# Import utility methods (wait_for_database, specifically)
. $(dirname $0)/bootstrap.util.sh

cd /var/nemo

# Run backend tests
test_nemo () {
    py.test --cov=/var/nemo/src/nemo --cov-report term --cov-report xml:/target/tests/nemo.coverage.xml /var/nemo/tests
}

# Run frontend tests
test_marlin () {
    yarn run jest --config tests/jest.config.js
}

# These make click happier about encoding. the default on 
# ubuntu is ascii, but we want utf-8
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

wait_for_database

# Test either frontend or backend if we have been told to do 
# so, otherwise test both.
if [ "$NEMO_TEST" = "nemo" ]; then
    test_nemo
elif [ "$NEMO_TEST" = "marlin" ]; then
    test_marlin
else
    test_nemo
    echo; echo; # for readability
    test_marlin
fi
