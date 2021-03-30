#!/bin/bash

# Setup default values
DEFAULT_FRONTEND_PORT="8080"

# Script cloud foundry
FRONTEND_PORT="${FRONTEND_PORT:=$DEFAULT_FRONTEND_PORT}"

manage.py runserver $DEFAULT_FRONTEND_PORT