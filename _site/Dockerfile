FROM ubuntu:12.04

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list  && apt-get -qq update && apt-get -y -qq upgrade && apt-get install -y software-properties-common wget sudo  python-setuptools build-essential python-dev htop ntp vim software-properties-common curl git-core apt-utils libreadline6 libreadline6-dev python-software-properties dialog locales  openssh-server net-tools rubygems ruby1.9.1-dev
RUN apt-get -qq -y clean
RUN gem update 
RUN echo "root:root" | chpasswd
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8
RUN gem install --no-rdoc --no-ri json jekyll

VOLUME ["/var/www/site"]
CMD "/usr/sbin/sshd" -D
EXPOSE 4000