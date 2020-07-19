FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    vim tcpdump curl iputils-ping net-tools netcat tzdata cron \
    python3.8
ENV PATH $PATH:/usr/bin/python3.8
ENV TZ Asia/Tokyo
ADD crontab /var/spool/crontab/root
RUN echo 'alias python="python3.8"' >> ~/.bashrc && \
    crontab /var/spool/crontab/root
COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]