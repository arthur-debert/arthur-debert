FROM ubuntu:12.04

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list  && apt-get -qq update && apt-get -y -qq upgrade && apt-get install -y software-properties-common wget sudo  python-setuptools build-essential python-dev htop ntp vim software-properties-common curl git-core apt-utils libreadline6 libreadline6-dev python-software-properties dialog locales  openssh-server net-tools 
RUN apt-add-repository ppa:brightbox/ruby-ng &&  apt-get -y -qq update
RUN apt-get remove rubygems
RUN apt-get install --force-yes -qq ruby1.9.3 
#RUN apt-get install -y -qq rubygems
RUN gem update 
RUN echo "root:root" | chpasswd
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8
RUN gem install --no-rdoc --no-ri json  jekyll jekyll-assets maruku rake sass uglifier github-pages therubyracer execjs bundler

VOLUME ["/var/www/source", "/var/www/build/"]
CMD "/usr/sbin/sshd" -D
EXPOSE 4000
EXPOSE 3001