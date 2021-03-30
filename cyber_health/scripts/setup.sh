#!/bin/bash

# Setup the virtual environment
python3 -m venv cyber-health-python

echo "Activating ./cyber-health-python/bin/activate"
# shellcheck disable=SC1091
source ./cyber-health-python/bin/activate

# Install dependencies
pip3 install -r requirements.txt

# NPM install dependencies
npm install
npm run frontend:build
