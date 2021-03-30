#!/bin/bash

# Setup default values
DEFAULT_FRONTEND_PORT="8080"

# Script cloud foundry
FRONTEND_PORT="${FRONTEND_PORT:=$DEFAULT_FRONTEND_PORT}"

# Setup the virtual environment
python3 -m venv cyber-health-python
# shellcheck disable=SC1091
source ./cyber-health-python/bin/activate

# Install dependencies
pip install -r requirements.txt

# NPM install dependencies
npm install
npm run frontend:build

# Start the application
python manage.py runserver $DEFAULT_FRONTEND_PORT