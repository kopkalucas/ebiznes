FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.8 python3-pip

RUN rm /usr/bin/python3 && ln -s /usr/bin/python3.8 /usr/bin/python3

CMD ["bash"]
