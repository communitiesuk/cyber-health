#!/bin/bash

# Setup default values
DEFAULT_FRONTEND_PORT="8080"

# Script cloud foundry
FRONTEND_PORT="${FRONTEND_PORT:=$DEFAULT_FRONTEND_PORT}"

# shellcheck disable=SC1091
source ./cyber-health-python/bin/activate

# Start the application
python manage.py runserver $DEFAULT_FRONTEND_PORT