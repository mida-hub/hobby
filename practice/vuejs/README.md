# nodejsのインストール
```
brew install nodebrew
nodebrew -v

// インストールできるNode.jsのバージョンの確認
nodebrew ls-remote

// ディレクトリの作成
mkdir -p ~/.nodebrew/src

// 安定版のNode.jsをインストール
nodebrew install-binary stable

// 使用できるNode.jsのバージョンを確認
nodebrew ls

// 使用するNode.jsのバージョンを指定
nodebrew use [インストールしたバージョン]

// nodeが使えるようにパスを通す
echo 'export PATH=$HOME/.nodebrew/current/bin:$PATH' >> ~/.zprofile

// 設定を反映させる
source ~/.zprofile

// Node.jsの実行確認
node -v
```

# Vue CLIのインストール
```
npm install -g @vue/cli@3.0.1 @vue/cli-service-global@3.0.1
npm install -g @vue/cli-init
vue --version
```

# Vuex のインストール
```
npm install vuex
```

# ビルド
```
vue serve App.vue --open
``` 

# プロジェクト
## プロジェクト作成
```
vue init webpack kanban-app
```

## アプリケーション起動確認
```
// 依存モジュールをインストール
npm install
// 開発モード
npm run dev
// UNITテスト
npm run unit
```

## プラグイン
### ESLint
```
npm install --save-dev eslint-plugin-vue@4.7.1
```

### APIサーバーの環境構築
```
npm install --save-dev body-parser
touch ./build/dev-server.js
```

### Vuex
```
npm install --save vuex es6-promise

mkdir -p src/store

touch src/store/index.js
touch src/store/mutation-types.js
touch src/store/mutations.js
touch src/store/getters.js
touch src/store/actions.js
```

### HTTPクライアントライブラリの導入
```
npm install --save axios

mkdir -p src/api

touch src/api/index.js
```

### Vue Test Utils
```
npm install --save-dev @vue/test-utils@1.0.0-beta.24
```

### Vue E2E Test
```
mkdir -p test/e2e/custom-commands

touch test/e2e/custom-commands/trigger.js
touch test/e2e/custom-commands/enterValue.js
```

## 単一ファイルコンポーネント化
### 単一ファイルコンポーネントの配置
```
mkdir -p src/components/{atoms,molecules,organsms,templates}

touch src/components/atoms/Kbn{Button,Icon}.vue
touch src/components/molecules/Kbn{LoginForm,BoardNavigation,TaskListHeader,TaskForm,TaskCard,TaskDetailForm}.vue
touch src/components/organsms/Kbn{BoardTask,TaskList}.vue
touch src/components/templates/Kbn{LoginView,BoardView,TaskDetailModal}.vue
```

### TemplatesコンポーネントにプレースホルダーのHTMLを実装
```
echo '<template>\n  <p>ログインページ</p>\n</template>' >> src/components/templates/KbnLoginView.vue
echo '<template>\n  <p>ボードページ</p>\n</template>' >> src/components/templates/KbnBoardView.vue
echo '<template>\n  <p>タスク詳細ページ</p>\n</template>' >> src/components/templates/KbnTaskDetailModal.vue
```

## バックエンドAPIとの通信のための準備
```
touch src/api/{auth,list,task}.js
```

## ルート定義
```
touch src/router/routes.js
```

## KbnButtonコンポーネント
```
mkdir -p test/unit/specs/components/atoms
touch test/unit/specs/components/atoms/KbnButton.spec.js

mkdir -p test/unit/specs/components/molecules
touch test/unit/specs/components/molecules/KbnLoginForm.spec.js

mkdir -p test/unit/specs/components/templates
touch test/unit/specs/components/templates/KbnLoginView.spec.js
```

## ログインアクションハンドラ
```
mkdir -p test/unit/specs/store/actions
touch test/unit/specs/store/actions/login.spec.js

mkdir -p test/unit/specs/store/mutations
touch test/unit/specs/store/mutations/auth_login.specs.js

mkdir -p test/unit/specs/api
touch test/unit/specs/api/auth.spec.js

touch src/api/client.js
```

## ルーティングの実装
```
mkdir -p test/unit/specs/router
touch test/unit/specs/router/guards.spec.js

touch src/router/guards.js
```


# 参考
## プロジェクト作成
cf. https://cr-vue.mio3io.com/guide/chapter7.html
cf. https://cr-vue.mio3io.com/guide/chapter8.html
```
vue create my-app
```

## ビルド
```
npm run serve
```
