# 実行
```
node app.js
```

# 実行時間
```
time node app.js
```

# プロファイル
```
node --prof app.js
```

# 解析
```
node --prof-process isolate-0x2660a40-v8.log
```

# パスワード bcrypt アルゴリズム
```
yarn global add htpasswd@2.4.0
htpasswd -D users.htpasswd admin
htpasswd -D users.htpasswd guest1
htpasswd -D users.htpasswd guest2
htpasswd -bB users.htpasswd admin apple
htpasswd -bB users.htpasswd guest1 1234
htpasswd -bB users.htpasswd guest2 5678
```