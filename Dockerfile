FROM ubuntu:focal
RUN apt update && apt install -y gnupg ruby-full wget 
RUN wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add -
RUN echo "deb https://packages.cloudfoundry.org/debian stable main" |  tee /etc/apt/sources.list.d/cloudfoundry-cli.list
RUN apt update && apt install -y cf7-cli
RUN gem install dpl --pre
