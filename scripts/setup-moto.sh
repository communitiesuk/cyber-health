#!/bin/bash
SERVICE="s3_mocks"
echo "Running in the folder $SERVICE"
cd "$SERVICE" || exit

python3 -m venv s3_mocks
echo "Activating ./s3_mocks/bin/activate"
source ./s3_mocks/bin/activate

# Ensure that we have the prerequisites
python3 -m pip install -U pipenv
python3 -m pip install -U pip

pip3 install wheel
pip3 install safety
pip3 install bandit

# Install dependencies
pip3 install -r requirements.txt
pipenv install

# start the server
moto_server s3
