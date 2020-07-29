FROM node:10.14.2
RUN apt-get update && apt-get install -y \
    vim less nkf postgresql
ENV LESSCHARSET utf-8
RUN yarn global add axios \
    && yarn global add yo@3.0.0 \
    && yarn global add generator-hubot \
    && yarn global add coffeescript@1.12.7 \
    && yarn global add pug@2.0.0-rc.4 \
    && yarn global add pug-cli \
    && yarn global add http-auth@3.2.3 \
    && yarn global add sequelize@5.21.5 \
    && yarn global add pg@7.17.1 \
    && yarn global add pg-hstore@2.3.3 \
    && yarn global add cookies@0.5.1 \
    && yarn global add moment-timezone@0.5.0 \
    && yarn global add clean-css@4.1.1 \
    && yarn global add htpasswd@2.4.0 \
    && yarn global add express-generator@4.16.0 \
    && yarn global add helmet@1.1.0 \
    && yarn global add passport@0.3.2 \
    && yarn global add passport-github2@0.1.9 \
    && yarn global add express-session@1.15.6 \
    && yarn global add jest@25.1.0 --dev \
    && yarn global add jest-junit@10.0.0 --dev \
    && yarn global add webpack@4.26.1 webpack-cli@3.1.2 @babel/core@7.1.6 @babel/preset-env@7.1.6 babel-loader@8.0.4 --dev \
    && yarn global add jquery@3.4.1

CMD ["/bin/bash"]
