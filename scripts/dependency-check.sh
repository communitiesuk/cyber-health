#!/bin/bash

APPLICATIONS=("cyber-health")

for application in "${APPLICATIONS[@]}"
do
    (
        echo "runnning dependency check on ./$application"
        dependency-check/bin/dependency-check.sh --project "$application" --scan "./$application" -f JSON 
        # --failOnCVSS 5
        # echo "Dependency Report"
        # cat dependency-check-report.json
    )
done