# AWS env
正しく設定できていればAWSアカウントが表示される

```
pip install awscli
aws --version

export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=

aws sts get-caller-identity --query Account --output text
```

# git-secrets
```
brew install git-secrets

git secrets --register-aws --global
git secrets --install ~/.git-templates/git-secrets
git config --global init.templatedir '~/.git-templates/git-secrets'
```

# terraform
## env
```
brew install terraform
terraform --version
```

### tfenv
```
brew install tfenv
tfenv --version
```

### list-remote
```
tfenv list-remote
tfenv install 0.12.5
tfenv install 0.12.4
```

### list
```
tfenv list
```

### use
```
tfenv use 0.12.5
```

### dockernized terraform
```
docker pull hashicorp/terraform:0.12.5
docker run --rm hashicorp/terraform:0.12.5 --version
```

## command
```
terraform init
terraform plan
terraform apply
terraform destroy
```
