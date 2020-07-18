FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    vim tcpdump curl iputils-ping net-tools netcat \
    python3.8
ENV PATH $PATH:/usr/bin/python3.8
RUN echo 'alias python="python3.8"' >> ~/.bashrc
CMD ["/bin/bash"]
