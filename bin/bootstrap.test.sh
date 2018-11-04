#!/bin/bash

cd /var/nemo

# Ping the dumb database until it's awake
while ! pg_isready -q -h db -d nemo -U nemo; do
    echo "bootstrap: waiting for database"
    sleep 2;
done
echo "bootstrap: atabase is ready"

# make click happier about encoding
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Run backend tests
cd /var/nemo
pytest /var/nemo/tests

# Couple lines on the terminal to seperate backend from frontend
echo
echo
echo

# Run frontend tests
./node_modules/.bin/jest --config tests/jest.config.js
