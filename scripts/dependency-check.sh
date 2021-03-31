#!/bin/bash

APPLICATIONS=("cyber_health")

for application in "${APPLICATIONS[@]}"
do
    (
        echo "runnning dependency check on ./$application"
        dependency-check/bin/dependency-check.sh --failOnCVSS 5 --disableAssembly --project "$application" --scan "./$application" -f JSON 
    )
done