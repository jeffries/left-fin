#!/bin/bash

echo "starting webpack dev server"
cd /var/nemo/marlin
/var/nemo/marlin/node_modules/.bin/webpack-dev-server --port 5001 --host 0.0.0.0 2>&1 | sed -e 's/^/webpack-dev-server: /' &

cd /var/nemo

# Ping the dumb database until it's awake
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
