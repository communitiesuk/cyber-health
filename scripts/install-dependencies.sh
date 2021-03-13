#!/bin/bash

sudo apt-get update
sudo apt-get install -y firefox-geckodriver wget unzip
gem install dpl --pre
npm install npm@latest -g
npm install http-server -g
wget https://github.com/jeremylong/DependencyCheck/releases/download/v6.1.2/dependency-check-6.1.2-release.zip
unzip dependency-check-6.1.2-release.zip
chmod 755 dependency-check/bin/*.sh
cd accessibility || exit
npm install
which firefox