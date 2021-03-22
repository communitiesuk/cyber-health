#!/bin/bash

# Create the database users expected
psql -c "create database $DATABASE_NAME;" -U postgres
psql -c "CREATE USER $DATABASE_USER WITH PASSWORD '$DATABASE_PASSWORD'" -U postgres ;

pg_isready -d "$DATABASE_NAME" -h "$DATABASE_HOST" -p "$DATABASE_PORT" -U "DATABASE_USER" -t 5

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