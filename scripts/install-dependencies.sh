#!/bin/bash

gem install dpl --pre
npm install http-server -g
cd accessibility || exit
npm install chromedriver --chromedriver_skip_download=true  
npm install