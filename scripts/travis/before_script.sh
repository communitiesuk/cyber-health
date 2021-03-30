#!/bin/bash

# shellcheck disable=SC1091
source scripts/setup-postgres.sh 

APPLICATIONS=("cyber_health")

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

        export SECRET_KEY="travis_secret_key_1"

        source setup.sh

        # Running the unit tests
        python manage.py test

        # shellcheck disable=SC1091
        source scripts/start.sh 
    )
done