#!/bin/bash

gem install dpl --pre
npm install npm@latest -g
npm install http-server -g
cd accessibility || exit
npm install chromedriver --chromedriver_skip_download=true --chromedriver_filepath=/usr/bin/google-chrome
npm install