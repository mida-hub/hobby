# 実用Go言語
## 「Goらしさ」に触れる
### 命名
#### 変数名
- 命名は Effective Go に従う
- maxLength のような命名
- 先頭小文字は非公開、先頭大文字は公開の場合
- 変数名は短いほうが良い。グローバルスコープの場合は長いほうが良い
- Go の型は静的に決まるので、変数名に型名を含める必要はない

#### パッケージ名
- encoding/json, encoding/xml のようにフォルダをわける
- テストの場合は _test という名前を用いる場合がある

#### インターフェース名
- er という接尾辞がついた名前を用いることがある

#### レシーバー名
- レシーバーの型を反映した名前をつける
- 1文字または2文字で十分
- Request であれば r のようなもので、プログラムを通して一貫した命名にする