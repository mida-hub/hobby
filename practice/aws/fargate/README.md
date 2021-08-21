# env
```
mkdir hello_ecs
cd hello_ecs4r
cdk init --language python
pipenv install -r ./requirements.txt --python 3.8.3
pipenv install aws-cdk --skip-lock
pipenv install aws-cdk.aws-ecs-patterns --skip-lock
cdk synth
cdk deploy
cdk destroy
```

# help
cdk synthでerrorになったとき
npm -g uninstall aws-cdk
npm -g install aws-cdk

aws cliを最新
