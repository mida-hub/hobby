# Express
## 環境

```
express --view=pug express-study
cd express-study
yarn install
cd ..
express --view=pug express-api
cd express-api
yarn install
```

## 起動
```
DEBUG=express-study:* PORT=8000 yarn start
DEBUG=express-study:*,module:* PORT=8000 yarn start
DEBUG=module:error PORT=8000 yarn start
```

## シークレット
```
node -e "console.log(require('crypto').randomBytes(8).toString('hex'));"
```