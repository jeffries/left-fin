#!/bin/bash

cd /var/nemo

# Ping the dumb database until it's awake
while ! pg_isready -q -h db -d nemo -U nemo; do
    echo "bootstrap: waiting for database"
    sleep 2;
done
echo "bootstrap: database is ready"

# make click happier about encoding
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

cd /var/nemo

if [ "$NEMO_TEST" = "nemo" ]; then
    # Run backend tests only
    pytest /var/nemo/tests
elif [ "$NEMO_TEST" = "marlin" ]; then
    # Run frontend tests only
    ./node_modules/.bin/jest --config tests/jest.config.js
else
    # Run all tests
    pytest /var/nemo/tests
    echo; echo; echo;
    ./node_modules/.bin/jest --config tests/jest.config.js
fi
