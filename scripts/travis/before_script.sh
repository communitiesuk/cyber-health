#!/bin/bash

# shellcheck disable=SC1091
# backing services
source scripts/setup-postgres.sh 
source scripts/setup-moto.sh

APPLICATIONS=("CyberHealth")

for application in "${APPLICATIONS[@]}"
do
    (
        echo "Running in the folder $application"
        cd "$application" || exit

        export SECRET_KEY="travis_secret_key_1"

        source scripts/setup.sh

        # shellcheck disable=SC1091
        source ./cyber-health-python/bin/activate

        # shellcheck disable=SC1091
        source scripts/start.sh 
    )
done