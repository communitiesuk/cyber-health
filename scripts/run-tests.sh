#!/bin/bash

APPLICATIONS=("CyberHealth")
for application in "${APPLICATIONS[@]}"
do
    (
        cd "$application" || exit 

        echo "Checking if the codebase is Python (has requirements.txt)"
        # Running safety check and bandit if the folder contains a requirements.txt
        if test -f "requirements.txt"; then
            echo "It is - So running bandit, safety and unit tests on the codebases"

            # shellcheck disable=SC1091
            source ./cyber-health-python/bin/activate
            
            if safety check -r requirements.txt; then
                echo "Failed: Safety Check for $application"
            else 
                 if ! bandit -r . -f json; then
                    echo "Failed: Bandit for $application"
                else 
                    echo "Running unit tests"
                    if ! python3 manage.py test; then
                        echo "Failed: unit tests for $application"
                    else 
                        echo "Passed: All direct tests for $application passed"
                    fi
                fi    
            fi
        fi

    )
  done  

TESTS=("accessibility" "acceptance")
for test in "${TESTS[@]}"
do
    (
        echo "Running the tests $test"
        cd "$test" || exit 
        if ! npm run test ; then
            echo "Failed: $test for $application"
        fi 
    )
done