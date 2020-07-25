FROM node:10.14.2
RUN apt-get update && apt-get install -y \
    vim less nkf postgresql
ENV LESSCHARSET utf-8
RUN yarn global add axios \
    && yarn global add yo@3.0.0 \
    && yarn global add generator-hubot \
    && yarn global add coffeescript@1.12.7 \
    && yarn add pug@2.0.0-rc.4 \
    && yarn global add pug-cli \
    && yarn add http-auth@3.2.3 \
    && yarn add sequelize@5.21.5 \
    && yarn add pg@7.17.1 \
    && yarn add pg-hstore@2.3.3 \
    && yarn add cookies@0.5.1 \
    && yarn add moment-timezone@0.5.0
# RUN useradd hubot -m
# USER hubot
# WORKDIR /home/hubot
# RUN yo hubot --defaults --adapter slack

# コンテナ接続後にサービスを立ち上げてdbコンテナに接続する
# service postgresql start
# su - postgres
# psql -h db -p 5432

CMD ["/bin/bash"]
