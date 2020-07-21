FROM node:10.14.2
RUN yarn global add axios \
    && yarn global add yo@3.0.0 \
    && yarn global add generator-hubot \
    && yarn global add coffeescript@1.12.7
RUN useradd hubot -m
USER hubot
WORKDIR /home/hubot/hubot-study
RUN yo hubot --defaults --adapter slack

CMD ["/bin/bash"]
