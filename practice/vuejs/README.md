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
vue --version
```