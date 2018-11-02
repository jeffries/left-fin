#!/bin/bash
# Ping the dumb database until it's awake

npx webpack-dev-server --port 5001 --host 127.0.0.1 2>&1 | sed -e 's/^/webpack-dev-server: /' &

while ! pg_isready -q -h db -d nemo -U nemo; do
    echo "waiting for database"
    sleep 2;
done
echo "database is ready"

# make click happier about encoding
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

export FLASK_APP=nemo
flask run --host=0.0.0.0
