#!/bin/bash

# shellcheck disable=SC1091
source scripts/setup-postgres.sh 

APPLICATIONS=("CyberHealth")

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

        source scripts/setup.sh

        # shellcheck disable=SC1091
        source ./cyber-health-python/bin/activate

        # Running the unit tests
        python3 manage.py test
        echo "***************************************1**********************************************"
        # shellcheck disable=SC1091
        source scripts/start.sh 
    )
done