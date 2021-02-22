# setup

```
npm install -g aws-cdk
cdk init app --language python
pipenv install -r requirements.txt
```

# setup2
https://console.aws.amazon.com/iam/home?region=ap-northeast-1#/security_credentials

```
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=ap-northeast-1
export AWS_DEFAULT_OUTPUT=JSON
```

# ssh key
```
export KEY_NAME="HirakeGoma"
aws ec2 create-key-pair --key-name ${KEY_NAME} --query 'KeyMaterial' --output text > ${KEY_NAME}.pem
chmod 400 HirakeGoma.pem
mv HirakeGoma.pem ~/.ssh/
```

# deploy
```
cdk deploy -c key_name="HirakeGoma"
```
