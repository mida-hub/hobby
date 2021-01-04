# jupyter ssl on amazon linux2
- cf.https://dev.classmethod.jp/articles/amazon-linux-2-jupyter-notebook/
- cf.https://blog.officekoma.co.jp/2017/05/aws-ec2-amazon-linux.html
- cf.https://sig9.hatenablog.com/entry/2019/10/28/000000

# ssh
```
ssh -i "jupyter.pem" ec2-user@xxx.xxx.xxx.xxx
```

# add jupyter user
```
sudo su -
useradd jupyter
passwd jupyter
cp -arp /home/ec2-user/.ssh /home/jupyter/
chown -R jupyter /home/jupyter/.ssh
visudo -f /etc/sudoers.d/90-cloud-init-users
```

# timezone
```
sudo cp /etc/localtime /etc/localtime.org
sudo ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

sudo vim /etc/sysconfig/clock
```

```
ZONE="Asia/Tokyo"
UTC=false
```

# pyenv
```
sudo yum -y install \
  bzip2 \
  bzip2-devel \
  gcc \
  git \
  libffi-devel \
  make \
  openssl \
  openssl-devel \
  readline \
  readline-devel \
  sqlite \
  sqlite-devel \
  zlib-devel

sudo curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

cat << 'EOS' >> ~/.bashrc
export PATH="/home/jupyter/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
EOS
source ~/.bashrc

pyenv install 3.8.2
pyenv global 3.8.2
```

# setup 2 jupyter 
```
pip install --upgrade pip
pip install jupyterlab

ipython3
In [1]: from IPython.lib import passwd
In [2]: passwd()
Enter password:<パスワードを入力>
Verify password:<もう一度パスワードを入力>
Out[2]: 'sha1:XXXXXXXXXXXXXXXXX'
Out[3]: quit()

mkdir ~/.jupyter
vim /home/jupyter/.jupyter/jupyter_notebook_config.py
```

```
c = get_config()
c.IPKernelApp.pylab = 'inline' #matplotlibで描画したものがJupyter Notebook上で表示可能となる
c.NotebookApp.ip = '0.0.0.0' #Jupyter NotebookにアクセスできるIPを制限
c.NotebookApp.open_browser = False #Jupyter Notebook起動後にブラウザの自動起動を拒否
c.NotebookApp.port = 8888 #ポート指定(デフォルト8888)
c.NotebookApp.password = 'sha1:XXXXXXXXXXXXXXXXX'
c.NotebookApp.notebook_dir = '/home/jupyter'
c.NotebookApp.base_url= '/jupyter'
```

# service
```
sudo vim /etc/systemd/system/jupyter.service
```

```
[Unit]
Desctiption = Jupyter lab
After = syslog.target

[Service]
Type = simple
WorkingDirectory = /home/jupyter
Restart = always
ExecStart = /home/jupyter/.pyenv/shims/jupyter lab --config=/home/jupyter/.jupyter/jupyter_notebook_config.py
base_url = /jupyter
User = jupyter
Group = jupyter

[Install]
WantedBy = multi-user.target
```

```
sudo systemctl enable jupyter
sudo systemctl start jupyter
sudo systemctl status jupyter
```

# setup nginx
```
sudo ln -s /lib/python2.7/site-packages/amazon_linux_extras ~/.pyenv/versions/3.8.2/lib/python3.8/site-packages/
sudo amazon-linux-extras install nginx1.12
sudo vim /etc/nginx/conf.d/jupyter.conf
```

```
map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
    listen 80 default_server;
    server_name localhost;
    root /usr/share/nginx/html;

    location /jupyter {
        proxy_pass http://localhost:8888;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_read_timeout 86400;
        proxy_set_header Origin "http://localhost:8888";
    }
}
```

```
sudo vim /etc/nginx/nginx.conf
```

```
listen 80 default_server;
listen [::]:80 default_server;
↓↓↓↓
#listen 80 default_server;
#listen [::]:80 default_server;
```

```
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl status nginx
```
