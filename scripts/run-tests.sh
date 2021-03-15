#!/bin/bash


TESTS=("accessibility" "acceptance")
for test in "${TESTS[@]}"
do
    (
        echo "Running the tests $test"
        cd "$test" || exit 
        npm run test
    )
done

# Run Static Analysis with Dependency Check 
# shellcheck disable=SC1091
# source scripts/dependency-check.sh 