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