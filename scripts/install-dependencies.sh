#!/bin/bash

sudo apt-get update
sudo apt-get install -y firefox-geckodriver
gem install dpl --pre
npm install npm@latest -g
npm install http-server -g
cd accessibility || exit
npm install
which firefox