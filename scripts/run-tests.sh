#!/bin/bash
set -e

APPLICATIONS=("CyberHealth")
for application in "${APPLICATIONS[@]}"
do
    (
        cd "$application" || exit 

        echo "Checking if the codebase is Python (has requirements.txt)"
        # Running safety check and bandit if the folder contains a requirements.txt
        if test -f "requirements.txt"; then
            echo "It is - So running bandit and safety on the codebases"
           safety check -r requirements.txt  --json
           bandit -r . -f json
        fi

        echo "Running unit tests"
        # Running the unit tests
        python3 manage.py test
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