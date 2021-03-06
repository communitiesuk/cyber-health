#!/bin/bash

# Setup the virtual environment
python3 -m venv cyber-health-python

echo "Activating ./cyber-health-python/bin/activate"
# shellcheck disable=SC1091
source ./cyber-health-python/bin/activate

# Ensure that we have the prerequisites
python3 -m pip install -U pipenv
python3 -m pip install -U pip
python3 -m pip install -U setuptools

pip3 install wheel
pip3 install safety
pip3 install bandit

# Install dependencies
pip3 install -r requirements.txt
pipenv install

# NPM install dependencies
npm install
npm run frontend:build

# run any django migrations required
python3 manage.py migrate

# load testdata
python3 manage.py loaddata */fixtures/testdata*.json

# copy all static files into STATIC_ROOT (static/assets)
python3 manage.py collectstatic --noinput
