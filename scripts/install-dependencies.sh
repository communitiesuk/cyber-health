#!/bin/bash

gem install dpl --pre
echo "updating node"
sudo apt-get -y install nodejs  
node -v
npm install -g npm@7.6.1
npm install http-server -g
cd accessibility || exit
npm install chromedriver --chromedriver_skip_download=true  
npm install