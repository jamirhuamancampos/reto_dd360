FROM ubuntu:latest

MAINTAINER Jamir Huaman

RUN apt-get update

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y software-properties-common

RUN add-apt-repository -y ppa:deadsnakes/ppa

RUN apt-get update

RUN apt-get install nano

RUN apt-get install -y python3.9-distutils

RUN apt-get install python3-apt

RUN apt-get install -y python3.9 python3-pip

RUN python3.9 --version

CMD python3.9 --version

CMD echo $(python3.9 --version)

RUN apt-get -y install cron

ADD cron.sh /root/cron.sh

RUN chmod 0644 /root/cron.sh

RUN touch /var/log/cron.log

RUN chmod 0644 /var/log/cron.log

RUN (crontab -l ; echo "* * * * * echo "Hello world" >> /var/log/cron.log") | crontab

RUN (crontab -l ; echo "*/5 * * * * /usr/bin/sh /root/cron.sh >> /var/log/cron.log") | crontab

RUN mkdir -p /var/log/app

VOLUME /var/log

WORKDIR /usr/app/src

COPY app.py ./

COPY requirements.txt ./

RUN python3.9 -m pip install -r requirements.txt

ENTRYPOINT cron start && tail -f /var/log/cron.log
