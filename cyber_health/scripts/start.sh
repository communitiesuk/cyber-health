#!/bin/bash

# Setup default values
DEFAULT_FRONTEND_PORT="8081"

# Script cloud foundry
FRONTEND_PORT="${FRONTEND_PORT:=$DEFAULT_FRONTEND_PORT}"

http-server -p 8081 . & # start a Web server, defaults on 0.0.0.0 (all interfaces) 
sleep 3 # give Web server some time to bind to sockets, etc