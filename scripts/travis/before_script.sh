#!/bin/bash

# shellcheck disable=SC1091
 source scripts/setup-postgres.sh 

APPLICATIONS=("cyber-health")
for application in "${APPLICATIONS[@]}"
do
    (
        echo "Running in the folder $application"
        cd "$application" || exit

        # Running safety check and bandit if the folder contains a requirements.txt
        if test -f "requirements.txt"; then
           safety check -r requirements.txt  --json
           bandit -r . -f json
        fi

        # shellcheck disable=SC1091
        source scripts/start.sh 


    )
done