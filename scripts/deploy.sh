#!/bin/bash

# Setup default values
DEFAULT_CLOUDFOUNDRY_API="https://api.london.cloud.service.gov.uk"
DEFAULT_CLOUDFOUNDRY_SPACE="sandbox"
DEFAULT_CLOUDFOUNDRY_ORG="mhclg-local-digital"

# Script cloud foundry
SCRIPT_CLOUDFOUNDRY_API="${CLOUDFOUNDRY_API:=$DEFAULT_CLOUDFOUNDRY_API}"
SCRIPT_CLOUDFOUNDRY_SPACE="${1:=$DEFAULT_CLOUDFOUNDRY_SPACE}"
SCRIPT_CLOUDFOUNDRY_ORG="${CLOUDFOUNDRY_SPACE:=$DEFAULT_CLOUDFOUNDRY_ORG}"

# Structure 
# The index is the name of each folder containing an application

APPLICATIONS=("frontend")

for application in "${APPLICATIONS[@]}"
do
    (
        cd "$application" || exit
        # shellcheck disable=SC1091
        source deploy.sh "$CLOUDFOUNDRY_USERNAME" "$CLOUDFOUNDRY_PASSWORD" "$SCRIPT_CLOUDFOUNDRY_API" "$SCRIPT_CLOUDFOUNDRY_SPACE" "$SCRIPT_CLOUDFOUNDRY_ORG"
    )
done