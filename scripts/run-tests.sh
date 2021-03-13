#!/bin/bash

# Run accessibility tests
node accessibility/index.js

# Run Static Analysis with Dependency Check 
# shellcheck disable=SC1091
source dependency-check.sh