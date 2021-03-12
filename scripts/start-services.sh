#!/bin/bash

APPLICATIONS=("frontend")

for application in "${APPLICATIONS[@]}"
do
    (
        cd "$application" || exit
        # shellcheck disable=SC1091
        source scripts/start.sh 
    )
done