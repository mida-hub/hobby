cf. https://github.com/peaceiris/actions-gh-pages

# コード解読
## やること
GitHub Actions で actions-gh-pages を利用したときに、gh-pages ブランチ作成からコミット、プッシュまでの流れを確認する

## なぜやるか
下記をどのように制御しているのか興味を持ったから

- gh-pages の存在を確認して、存在しなければブランチを作成する
- どうやってブランチを切り替えて、ファイルをコミット、プッシュする

## 処理の流れ
1. nextjs build
2. gh-pages@v3 を使って、out フォルダをもとに gt-pages ブランチにコミット＆プッシュ＋諸々の設定をする
3. 指定のブランチにプッシュされると、GitHub Pages の機能として、自動的に GitHub Actions が起動されてホスティング用のサイトがデプロイされる

https://docs.github.com/ja/pages/getting-started-with-github-pages/about-github-pages#publishing-sources-for-github-pages-sites

### gh-pages@v3 詳細
1. inputs を取得する
2. auth を設定する
3. gh-pages を clone, 存在しなければ branch を作成する
4. git rm -r --ignore-unmatch * で clone したファイルを削除する
5. out -> clone 先ディレクトリにコピーする
6. git add --all で差分がステージングに追加される
7. commit & push

## 解読
### ソースファイルの特定
- GitHub Actions は action.yml に起動方法が記載されているので action.yml を読む
- action.yml の main では lib/index.js を実行している
- リポジトリ上に lib フォルダはない
- src 配下を確認すると index.ts がある
- tsconfig.json を確認すると、rootDir は ./src 、outDir は ./lib となっている。コンパイル時に lib/index.js が出力される
- src/index.ts は main.ts を実行している

### GitHub Actions (peaceiris/actions-gh-pages@v3) の log
下記コマンドで gt-pages ブランチをクローンする

#### 初回 clone
初回は gh-pages ブランチが存在しないので、エラーをキャッチしてブランチを作成している
```bash
  [INFO] ForceOrphan: false
  /usr/bin/git clone --depth=1 --single-branch --branch gh-pages ***github.com/mida-hub/blog.git /home/runner/actions_github_pages_1661412127168
  Cloning into '/home/runner/actions_github_pages_1661412127168'...
  warning: Could not find remote branch gh-pages to clone.
  fatal: Remote branch gh-pages not found in upstream origin
  [INFO] first deployment, create new branch gh-pages
  [INFO] The process '/usr/bin/git' failed with exit code 128
  [INFO] chdir /home/runner/actions_github_pages_1661412127168
  /usr/bin/git init
  /usr/bin/git checkout --orphan gh-pages
```

#### コミット&プッシュ
- clone したファイルを削除
- nextjs の build 先の out から clone 先にコピー
- コミット&プッシュ

```bash
Prepare publishing assets
  /usr/bin/git rm -r --ignore-unmatch *
  [INFO] chdir /home/runner/actions_github_pages_1661605152280
  [INFO] prepare publishing assets
  [INFO] copy /home/runner/work/blog/blog/out to /home/runner/actions_github_pages_1661605152280
  [INFO] delete excluded assets

Setup Git config
  /usr/bin/git remote rm origin
  /usr/bin/git remote add origin ***github.com/mida-hub/blog.git
  /usr/bin/git add --all
  /usr/bin/git config user.name mida-hub
  /usr/bin/git config user.email mida-hub@users.noreply.github.com

Create a commit
  /usr/bin/git commit -m deploy: (hash値)

Push the commit or tag
  /usr/bin/git push origin gh-pages
```

### GitHub Actions (actions/checkout@v2) の log
気になったので checkout についても調査。存在するブランチじゃないと checkout できない

```bash
Getting Git version info
  /usr/bin/git version

Initializing the repository
  /usr/bin/git init /home/runner/work/blog/blog
  /usr/bin/git remote add origin https://github.com/mida-hub/blog

Disabling automatic garbage collection
  ...
Setting up auth
  ...
Fetching the repository
  /usr/bin/git -c protocol.version=2 fetch --no-tags --prune --progress --no-recurse-submodules --depth=1 origin +refs/heads/gh-pages*:refs/remotes/origin/gh-pages* +refs/tags/gh-pages*:refs/tags/gh-pages*
   * [new branch]      gh-pages   -> origin/gh-pages

Determining the checkout info
  /usr/bin/git branch --list --remote origin/gh-pages

Checking out the ref
  /usr/bin/git checkout --progress --force -B gh-pages refs/remotes/origin/gh-pages
```
