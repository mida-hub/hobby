FROM node:19-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git ca-certificates && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/* && \
    npm install -g npm@9.2.0 && \
    git clone https://github.com/evidence-dev/template.git my-project && \
    cd my-project && \
    npm install && \
    rm -rf { .git .github .gitignore }

COPY package.json /app/my-project
