#!/bin/bash

# Create the database users expected along with databases
sudo -u postgres psql postgres -c "CREATE USER $DATABASE_USER WITH PASSWORD '$DATABASE_PASSWORD' CREATEDB;"
sudo -u postgres psql postgres -c "CREATE DATABASE $DATABASE_NAME OWNER $DATABASE_USER;"

echo "Confirm database is running: pg_isready"
pg_isready -d "$DATABASE_NAME" -U "$DATABASE_USER" -t 5

APPLICATIONS=("cyber-health")
for application in "${APPLICATIONS[@]}"
do
    (
        echo "Running in the folder $application"
        cd "$application" || exit
        # shellcheck disable=SC1091
        source scripts/start.sh 
    )
done