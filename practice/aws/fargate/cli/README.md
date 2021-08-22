# Amazon ECS CLI
cf. https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ECS_CLI_installation.html

```
sudo curl -Lo /usr/local/bin/ecs-cli https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-darwin-amd64-latest
brew install gnupg
gpg --keyserver hkp://keys.gnupg.net --recv BCE9D9A42D51784F
curl -Lo ecs-cli.asc https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-darwin-amd64-latest.asc
curl -Lo ecs-cli.asc https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-darwin-amd64-latest.asc
gpg --verify ecs-cli.asc /usr/local/bin/ecs-cli
sudo chmod +x /usr/local/bin/ecs-cli
```

# tutorial
## step 1
```
aws iam --region ap-northeast-1 create-role --role-name ecsTaskExecutionRole --assume-role-policy-document file://task-execution-assume-role.json
aws iam --region ap-northeast-1 attach-role-policy --role-name ecsTaskExecutionRole --policy-arn arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
```

## step 2
```
ecs-cli configure --cluster tutorial --default-launch-type FARGATE --config-name tutorial --region ap-northeast-1
ecs-cli configure profile --access-key AWS_ACCESS_KEY_ID --secret-key AWS_SECRET_ACCESS_KEY --profile-name tutorial-profile
```

## step 3
```
ecs-cli up --cluster-config tutorial --ecs-profile tutorial-profile
aws ec2 describe-security-groups --filters Name=vpc-id,Values=VPC_ID --region ap-northeast-1
aws ec2 authorize-security-group-ingress --group-id security_group_id --protocol tcp --port 80 --cidr 0.0.0.0/0 --region ap-northeast-1
```

## step 5
```
ecs-cli compose --project-name tutorial service up --create-log-groups --cluster-config tutorial --ecs-profile tutorial-profile
```
