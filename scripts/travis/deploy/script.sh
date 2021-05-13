#!/bin/bash

# Script cloud foundry
SCRIPT_CLOUDFOUNDRY_API="${CLOUDFOUNDRY_API:=$DEFAULT_CLOUDFOUNDRY_API}"
SCRIPT_CLOUDFOUNDRY_SPACE="${1}"
SCRIPT_CLOUDFOUNDRY_ORG="${CLOUDFOUNDRY_ORG:=$DEFAULT_CLOUDFOUNDRY_ORG}"

# Structure 
# The index is the name of each folder containing an application

APPLICATIONS=("CyberHealth")

for application in "${APPLICATIONS[@]}"
do
    (
        cd "$application" || exit
        if [ "$SCRIPT_CLOUDFOUNDRY_SPACE" == "production" ]; then
            SCRIPT_APP_NAME="$application"
        else
            SCRIPT_APP_NAME=$(echo "$application-$SCRIPT_CLOUDFOUNDRY_SPACE" | tr '[:upper:]' '[:lower:]')
        fi
        # shellcheck disable=SC1091
        source scripts/deploy.sh "$CLOUDFOUNDRY_USERNAME" "$CLOUDFOUNDRY_PASSWORD" "$SCRIPT_CLOUDFOUNDRY_API" "$SCRIPT_CLOUDFOUNDRY_SPACE" "$SCRIPT_CLOUDFOUNDRY_ORG" "$SCRIPT_APP_NAME"
    )
done