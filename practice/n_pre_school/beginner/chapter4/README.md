# Express
## 環境

```
express --view=pug schedule-arranger
cd schedule-arranger
yarn install
```

## 起動
```
PORT=8000 yarn start
DEBUG=schedule-arranger:* PORT=8000 yarn start
DEBUG=schedule-arranger:*,module:* PORT=8000 yarn start
DEBUG=module:error PORT=8000 yarn start
```

## webpack
```
npx webpack
or
node node_modules/webpack/bin/webpack.js
```

## セキュリティ対策
### X-Powered-By ヘッダの除去
X-Powered-By ヘッダは、この Web サービスがどのようなフレームワークや アプリケーションにより作られているかを表示するヘッダ
フレームワークに脆弱性が見つかった時に、攻撃対象にされる危険性がある

```
yarn add helmet@3.8.2
```

## OAuth
### GitHub認証の実装
```
yarn add passport@0.3.2
yarn add passport-github2@0.1.9
yarn add express-session@1.13.0
```

### session 関数に渡すオブジェクトの secret 値を生成する
```
node
console.log(require('crypto').randomBytes(8).toString('hex'));"
```

## Router オブジェクトをテストする
```
yarn add jest@25.1.0 --dev
yarn add supertest@3.1.0 --dev
yarn add passport-stub@1.1.1 --dev
```

package.json
```
  "scripts": {
    "start": "node ./bin/www",
    "test": "npx jest --testTimeout=10000 --forceExit"
  },
```

### テストコードの作成
```
mkdir test
touch test/test.js
yarn test
```