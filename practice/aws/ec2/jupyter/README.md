# jupyter ssl on ubuntu
cf.https://gist.github.com/sean-smith/f6bd44f0f9eb785e944e7fd999d7b076
cf.https://qiita.com/ground0state/items/6d5c96dd14a5cb256f64
cf.https://dev.classmethod.jp/articles/amazon-linux-2-jupyter-notebook/
cf.https://qiita.com/tontonyoga/items/7c7662b61220c86195c9
cf.https://qiita.com/tigersun2000/items/1091299b675efeb2c6ee

# キーペアの権限変更
```
chmod 600 jupyter.pem
```

# ssh
```
ssh -i "jupyter.pem" ec2-user@xxx.xxx.xxx.xxx
```

# setup jupyter
```
sudo amazon-linux-extras install python3
sudo python3 -m pip install --upgrade pip
sudo python3 -m pip install jupyter
sudo python3 -m pip install jupyterlab
```

# add jupyter user
```
sudo useradd jupyter
sudo passwd jupyter
```

# service
```
sudo vim /etc/systemd/system/jupyter.service
```

[Unit]
Desctiption = Jupyter lab
After = syslog.target

[Service]
Type = simple
WorkingDirectory = /home/jupyter
Restart = always
ExecStart = /usr/bin/jupyter lab --ip=127.0.0.1 --no-browser --NotebookApp.
base_url=/jupyter
User = jupyter
Group = jupyter

[Install]
WantedBy = multi-user.target

```
sudo systemctl enable jupyter
sudo systemctl start jupyter
sudo systemctl status jupyter
```

# setup nginx
```
sudo amazon-linux-extras install nginx1.12
sudo vim /etc/nginx/conf.d/jupyter.conf
```

map $http_upgrade $connection_upgrade {
    default upgrade;
    '' close;
}

server {
    listen 80 default_server;
    server_name your_domain;
    root /usr/share/nginx/html;

    location /jupyter {
        proxy_pass http://localhost:8888;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_read_timeout 86400;
        proxy_set_header Origin "http://localhost:8888";
    }

    location ^~ /.well-known/acme-challenge/ {
        root /usr/share/nginx/html;
    }
}

```
sudo vim /etc/nginx/nginx.conf
```

listen 80 default_server;
listen [::]:80 default_server;
↓↓↓↓
#listen 80 default_server;
#listen [::]:80 default_server;

```
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl status nginx
```

# Certbot
```
sudo amazon-linux-extras install -y epel
sudo yum install certbot
certbot certonly --webroot --webroot-path /usr/share/nginx/html -d your_domain
```

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/your_domain/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/your_domain/privkey.pem
   Your cert will expire on 2021-03-26. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot
   again. To non-interactively renew *all* of your certificates, run
   "certbot renew"
 - If you like Certbot, please consider supporting our work by:

   Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
   Donating to EFF:                    https://eff.org/donate-le

# nginx
SSL対応

```
sudo vim /etc/nginx/conf.d/jupyter.conf
```

ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
server {
    listen 443;
    ssl on;
    server_name your_domain;
    root /usr/share/nginx/html;
    ssl_certificate /etc/letsencrypt/live/your_domain/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/your_domain
    /privkey.pem; # managed by Certbot

    location /jupyter {
        proxy_pass http://localhost:8888;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection $connection_upgrade;
        proxy_read_timeout 86400;
        proxy_set_header Origin "http://localhost:8888";
    }
}

# setup 2 jupyter 
ipython3
In [1]: from IPython.lib import passwd
In [2]: passwd()
Enter password:<パスワードを入力>
Verify password:<もう一度パスワードを入力>
Out[2]: 'sha1:XXXXXXXXXXXXXXXXX'
Out[3]: quit()

```
jupyter-notebook --generate-config
vi /home/jupyter/.jupyter/jupyter_notebook_config.py
```

c = get_config()
c.IPKernelApp.pylab = 'inline' #matplotlibで描画したものがJupyter Notebook上で表示可能となる
c.NotebookApp.ip = '0.0.0.0' #Jupyter NotebookにアクセスできるIPを制限
c.NotebookApp.open_browser = False #Jupyter Notebook起動後にブラウザの自動起動を拒否
c.NotebookApp.port = 8888 #ポート指定(デフォルト8888)
c.NotebookApp.password = 'sha1:XXXXXXXXXXXXXXXXX'
c.NotebookApp.notebook_dir = '/home/jupyter'
c.NotebookApp.base_url= '/jupyter'

[Service]
Type = simple
WorkingDirectory = /home/jupyter
Restart = always
ExecStart = /usr/bin/jupyter lab --config=/home/jupyter/.jupyter/jupyter_notebook_config.py
User = jupyter
Group = jupyter
