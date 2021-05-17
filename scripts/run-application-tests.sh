#!/bin/bash

error_code=1

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
            
            if ! safety check -r requirements.txt; then
                echo "Failed: Safety Check for $application"
                return $error_code
            else 
            
                if ! bandit -r . -x ./cyber-health-python; then
                    echo "Failed: Bandit for $application"
                    return $error_code
                else 
                    echo "Running unit tests"
                    if ! python3 manage.py test; then
                        echo "Failed: unit tests for $application"
                        return $error_code
                    else 
                        echo "Passed: All direct tests for $application passed"
                    fi
                fi    
            fi
        fi

    )
done

# return with whatever exit code comes back from tests
return $?
