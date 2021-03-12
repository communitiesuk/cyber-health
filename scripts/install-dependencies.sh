#!/bin/bash

gem install dpl --pre
sudo apt-get -y install nodejs  
npm install -g npm@7.6.1
npm install http-server -g
cd accessibility || exit
npm install chromedriver --chromedriver_skip_download=true  
npm install