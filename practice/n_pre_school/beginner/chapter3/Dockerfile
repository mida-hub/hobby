FROM node:10.14.2
RUN apt-get update && apt-get install -y \
    vim less nkf
RUN yarn global add axios \
    && yarn global add yo@3.0.0 \
    && yarn global add generator-hubot \
    && yarn global add coffeescript@1.12.7 \
    && yarn add pug@2.0.0-rc.4 \
    && yarn global add pug-cli
RUN useradd hubot -m
USER hubot
WORKDIR /home/hubot
ENV LESSCHARSET utf-8
# RUN yo hubot --defaults --adapter slack

CMD ["/bin/bash"]
