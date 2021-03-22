#!/bin/bash

# Create the database users expected
psql -c "create database $DATABASE_NAME;" -U postgres

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