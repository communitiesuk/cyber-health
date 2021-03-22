#!/bin/bash

# Create the database users expected
psql -c 'create database travis_ci_test;' -U postgres
psql -c "CREATE USER travis WITH PASSWORD 'travispass'" -U postgres ;

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