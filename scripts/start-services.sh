#!/bin/bash

APPLICATIONS=("frontend")

pwd

for application in "${APPLICATIONS[@]}"
do
    (
        echo "Running in the folder $application"
        cd "$application" || exit
        # shellcheck disable=SC1091
        source scripts/start.sh 
    )
done