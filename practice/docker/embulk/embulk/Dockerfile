FROM openjdk:8-slim

ENV LANG ja_JP.UTF-8 \
    LANGUAGE ja_JP:ja \
    LC_ALL ja_JP.UTF-8 \
    TZ JST-9

# vim, ping などをインストール
RUN apt-get update \
    && apt-get install -y iputils-ping net-tools curl vim default-mysql-client \
    && apt-get clean \
    && rm -rf \
        /var/lib/apt/lists/* \
        /tmp/* \
        /var/tmp/* \
# Embulk をインストール
    && curl --create-dirs -o ~/.embulk/bin/embulk -L "https://dl.embulk.org/embulk-latest.jar" \
    && chmod +x ~/.embulk/bin/embulk \
    && echo 'export PATH="$HOME/.embulk/bin:$PATH"' >> ~/.bashrc \
    && . ~/.bashrc \
# mysql用のプラグインをインストール
    && ~/.embulk/bin/embulk gem install embulk-input-mysql \
    && ~/.embulk/bin/embulk gem install embulk-output-bigquery

WORKDIR /root

COPY ./conf ./conf
