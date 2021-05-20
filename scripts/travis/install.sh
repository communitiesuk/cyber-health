#!/bin/bash

gem install dpl --pre
npm install npm@latest -g
npm install http-server -g
wget "https://github.com/jeremylong/DependencyCheck/releases/download/v$DEPENDENCY_CHECK_VERSION/dependency-check-$DEPENDENCY_CHECK_VERSION-release.zip"
unzip "dependency-check-$DEPENDENCY_CHECK_VERSION-release.zip"
chmod 755 dependency-check/bin/*.sh

TESTS=("accessibility" "acceptance")
for test in "${TESTS[@]}"
do
    (
        cd "$test" || exit
        export TEST_USERNAME=$TEST_USERNAME
        export TEST_PASSWORD=$TEST_PASSWORD
        npm install
    ) 
done