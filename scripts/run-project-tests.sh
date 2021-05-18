#!/bin/bash

error_code=1

TESTS=("accessibility" "acceptance")
for test in "${TESTS[@]}"
do
    (
        echo "Running the tests $test"
        cd "$test" || exit 
        if ! npm run test ; then
            echo "Failed: $test for $application"
            return $error_code
        fi 
    )
done

# return with whatever exit code comes back from tests
return $?