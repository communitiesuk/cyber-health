#!/bin/bash

# Run Accessibility and Acceptance tests
# shellcheck disable=SC1091
 source scripts/run-tests.sh 

# Run Static Analysis with Dependency Check 
# shellcheck disable=SC1091
 source scripts/dependency-check.sh 