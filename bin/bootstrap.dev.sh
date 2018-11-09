#!/bin/bash

# Import utility methods (wait_for_database, specifically)
. $(dirname $0)/bootstrap.util.sh

cd /var/nemo

start_webpack_dev_server () {
    echo "starting webpack dev server"

    # This line will start the webpack dev server on 0.0.0.0:5001,
    # redirect stderr to stdout, and configure sed to prepend each
    # line with "webpack-dev-server: ", and put that entire job in
    # the background.
    yarn run webpack-dev-server --port 5001 --host 0.0.0.0 2>&1 | sed -e 's/^/webpack-dev-server: /' &
}

# Start webpack server first, so it can spin up while we're
# waiting for the database.
start_webpack_dev_server
wait_for_database

# These make click happier about encoding. the default on 
# ubuntu is ascii, but we want utf-8
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

# Start the application on 0.0.0.0:5000
export FLASK_APP=nemo
flask run --host=0.0.0.0
