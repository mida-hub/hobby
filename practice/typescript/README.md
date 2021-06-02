# setup
```
npm install -g typescript
```

nodebrewの反映
```
source ~/.zprofile
```

# use promise
tsconfig.json の target/module/libを変更する
コーディング上はエラーが出なくなるがコンパイル時にエラーが出る
下記のようなオプションを指定することでエラーが出なくなる

```
tsc sample_promise.ts --lib es2015,dom
```
