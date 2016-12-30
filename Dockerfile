FROM ubuntu
MAINTAINER Matthew Fleeger

RUN apt-get update && apt-get install -y curl wget unzip python python-pip xvfb xterm

RUN mkdir -p /root/util
RUN mkdir -p /root/test

ADD ./util/ /root/util
ADD ./test/ /root/test

RUN bash /root/util/install_chrome.sh
RUN bash /root/util/install_webdriver.sh

RUN pip install selenium tinys3

CMD cd /root && xvfb-run -s "-screen 0 1024x768x16" test/test1.py
