#!/bin/bash

# Setup default values
DEFAULT_FRONTEND_PORT="8000"

# Script cloud foundry
FRONTEND_PORT="${FRONTEND_PORT:=$DEFAULT_FRONTEND_PORT}"

python3 -m venv cyber-health-python
# shellcheck disable=SC1091
source ./cyber-health-python/bin/activate 

# Install dependencies
pip install -r requirements.txt

# NPM install dependencies
npm install
npm run frontend:build

# Start python
python manage.py runserver