# docker環境にサーバーを立てて、ローカルと通信する
```
docker-compose up -d
docker-compose exec n_pre_school bash
cd /work/httpd
python -m http.server 8000
```

# ローカルPC
```
curl http://localhost:8000/index.html
```