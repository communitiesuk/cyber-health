#!/bin/bash

echo "Building frontend assets before deployment"
# Repeat frontend:build in order to populate dist folder on assets
npm install --silent
npm run frontend:build

echo "Deploying to Gov.uk PAAS"
# Deploy code to cloud foundry
dpl cloudfoundry --username "$1" --password "$2" --api "$3" --space "$4" --organization "$5" --app_name "$6"
