# jupyter ssl on ubuntu
cf.https://gist.github.com/sean-smith/f6bd44f0f9eb785e944e7fd999d7b076

# キーペアの権限変更
```
chmod 600 jupyter.pem
```

# ssh
```
ssh -i "jupyter.pem" ubuntu@ec2-18-183-147-216.ap-northeast-1.compute.amazonaws.com
```

# setup python
```
mkdir jupyter
sudo su -
apt update && apt install -y --no-install-recommends \
        build-essential \
        libffi-dev \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
touch ~/.bash_profile
echo -e "# pyenv paths" >> ~/.bash_profile
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile
pyenv install 3.8.2
pyenv global 3.8.2
pip install --upgrade pip
pip install jupyterlab
```

# Certbot
```
add-apt-repository ppa:certbot/certbot
apt-get update
apt-get install certbot
```

# Certificate
```
mkdir -p /root/.key
cd /root/.key
certbot certonly --webroot -w /home/ubuntu/jupyter -d hogehoge
```
