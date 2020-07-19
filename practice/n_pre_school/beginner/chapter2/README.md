# docker環境にサーバーを立てる
```
docker-compose up -d
docker-compose exec n_pre_school bash
```

# ローカルと通信する
```
cd /work
mkdir httpd
cd httpd
python -m http.server 8000
```

# ローカルPCから
```
curl http://localhost:8000/index.html
```

# bot
```
cd /work
mkdir bot
cd bot
touch niconico-ranking.sh
chmod a+x niconico-ranking.sh
sh ./niconico-ranking.sh
```

# cron
## Dockerfile
```
ADD crontab /var/spool/crontab/root
RUN crontab /var/spool/crontab/root
```

## entrypoint.sh
```
/etc/init.d/cron restart
tail -f /dev/null
※コンテナプロセスが終了しないようにするコマンド
```
