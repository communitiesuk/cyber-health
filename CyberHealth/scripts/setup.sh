#!/bin/bash

# Ensure that we have the prerequisites
pipenv shell
pipenv install -U setuptools
pipenv install wheel
pipenv install whitenoise

# Install dependencies
pipenv install -r requirements.txt

# NPM install dependencies
npm install
npm run frontend:build
