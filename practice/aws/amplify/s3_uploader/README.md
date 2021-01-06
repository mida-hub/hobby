# amplify
cf.https://dev.classmethod.jp/articles/amplify-s3-upload/

## setup
```
git clone https://github.com/aws-samples/aws-amplify-vue.git
cd aws-amplify-vue
npm install
npm install -g npm
npm add element-ui
npm install moment-timezone
```

## create aws resource
```
npm install -g @aws-amplify/cli
amplify init
amplify add auth
amplify add storage
amplify push
npm run dev
```

## todo
- upload時
  - timestamp付与
    - 同じファイル名の挙動を確認
- route設定
  - 動的にアップロードできるようにする
  - keyをパースする
  - ディレクトリを無視するようにする
- ルートアクセス時
  - 何もさせないようにする
