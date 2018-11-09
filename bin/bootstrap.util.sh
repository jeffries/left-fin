# Bootstrap utilities

# Ping the Postgres database until it's ready to accept connections
wait_for_database () {
    while ! pg_isready -q -h db -d nemo -U nemo; do
        echo "bootstrap: waiting for database"
        sleep 2;
    done
    echo "bootstrap: database is ready"
}
