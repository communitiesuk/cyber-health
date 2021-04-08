#!/bin/bash

# Ensure that we have the prerequisites
python3 -m pip install -U pipenv
python3 -m pip install -U setuptools
pip3 install wheel
pip3 install whitenoise

# Install dependencies
pipenv shell
pipenv install -r requirements.txt

# NPM install dependencies
npm install
npm run frontend:build
