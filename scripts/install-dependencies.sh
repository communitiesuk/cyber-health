#!/bin/bash

gem install dpl --pre
npm install npm@latest -g
npm install http-server -g
apt-get install firefox-geckodriver
cd accessibility || exit
npm install
which firefox