#!/bin/bash

APPLICATIONS=("CyberHealth")
for application in "${APPLICATIONS[@]}"
do
    (
        cd "$application" || exit 

        echo "Checking if the codebase is Python (has requirements.txt)"
        # Running safety check and bandit if the folder contains a requirements.txt
        if test -f "requirements.txt"; then
            echo "It is - So running bandit and safety on the codebases"

            # shellcheck disable=SC1091
            source ./cyber-health-python/bin/activate
            
            safety check -r requirements.txt  --json
            
            bandit -r . -f json

            echo "Running unit tests"
            python3 manage.py test

        fi

    )
  done  

TESTS=("accessibility" "acceptance")
for test in "${TESTS[@]}"
do
    (
        echo "Running the tests $test"
        cd "$test" || exit 
        npm run test
    )
done