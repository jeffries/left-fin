#!/bin/bash
# Ping the dumb database until it's awake

while ! pg_isready -q -h db -d nemo -U nemo; do
    echo "waiting for database"
    sleep 2;
done
echo "database is ready"

flask run --host=0.0.0.0
