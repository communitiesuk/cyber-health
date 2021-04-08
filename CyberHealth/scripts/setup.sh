#!/bin/bash
echo "*************************************************************************************************************"
# Setup the virtual environment
python3 -m venv cyber-health-python

echo "Activating ./cyber-health-python/bin/activate"
# shellcheck disable=SC1091
source ./cyber-health-python/bin/activate
echo "*************************************************************************************************************"
# Ensure that we have the prerequisites
python3 -m pip install -U pipenv
python3 -m pip install -U pip
python3 -m pip install -U setuptools
pip3 install wheel
pip3 install whitenoise
echo "*************************************************************************************************************"
# Install dependencies
pip3 install -r requirements.txt
pipenv install
echo "*************************************************************************************************************"
# NPM install dependencies
npm install
npm run frontend:build
echo "*************************************************************************************************************"