FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    vim tcpdump curl iputils-ping net-tools netcat tzdata cron less \
    python3.8

ENV PATH $PATH:/usr/bin/python3.8
ENV TZ Asia/Tokyo
ENV NODE_VERSION 10.14.2

# Replace Shell with bash so we can source files
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
WORKDIR /work/my-first-node-js
RUN echo 'alias python="python3.8"' >> ~/.bashrc \    
    && curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.34.0/install.sh | bash \
    && source ~/.bashrc \
    && . $HOME/.nvm/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default \
    && curl -o- -L https://yarnpkg.com/install.sh | bash -s -- --version 1.21.1 \
    && source ~/.bashrc \
    && /root/.yarn/bin/yarn add axios

CMD ["/bin/bash"]
