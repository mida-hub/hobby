# AWSによるクラウド入門
https://tomomano.gitlab.io/intro-aws/

## setup
https://console.aws.amazon.com/iam/home?region=ap-northeast-1#/security_credentials
```
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=ap-northeast-1
export AWS_DEFAULT_OUTPUT=JSON
```

### aws cli
https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2-mac.html#cliv2-mac-install-gui

```
curl "https://awscli.amazonaws.com/AWSCLIV2-2.0.30.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
aws --version
aws configure
```

### aws cdk
```
npm install -g aws-cdk
cdk --version
cdk bootstrap
```

### ssh key
```
export KEY_NAME="HirakeGoma"
aws ec2 create-key-pair --key-name ${KEY_NAME} --query 'KeyMaterial' --output text > ${KEY_NAME}.pem
chmod 400 HirakeGoma.pem
mv HirakeGoma.pem ~/.ssh/
```

## deploy
```
cdk deploy -c key_name="HirakeGoma"
```

## ssh
```
ssh -i ~/.ssh/HirakeGoma.pem ec2-user@54.249.7.176
sudo yum update -y
sudo yum install -y python36
```

## destroy
```
cdk destroy
aws ec2 delete-key-pair --key-name "HirakeGoma"
rm -f ~/.ssh/HirakeGoma.pem
```
