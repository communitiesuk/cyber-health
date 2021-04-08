#!/bin/bash

APPLICATIONS=("CyberHealth")

for application in "${APPLICATIONS[@]}"
do
    (
        echo "running dependency check on ./$application"
        dependency-check/bin/dependency-check.sh --failOnCVSS 8 --disableAssembly --project "$application" --scan "./$application" -f JSON 
    )
done