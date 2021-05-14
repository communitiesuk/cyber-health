#!/bin/bash

exit_on_error() {
  if [ "$1" -ne 0 ]; then
    exit $1
  fi
}

# Run Safety, Bandit and unit tests
# shellcheck disable=SC1091
source scripts/run-application-tests.sh
exit_on_error "$?"

# Run Accessibility and Acceptance tests
# shellcheck disable=SC1091
source scripts/run-project-tests.sh
exit_on_error "$?"

# Run Static Analysis with Dependency Check 
# shellcheck disable=SC1091
source scripts/dependency-check.sh 
exit_on_error "$?"