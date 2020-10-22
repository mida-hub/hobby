# 生成に関するパターン
## Builder
### 概要
- 作成されるオブジェクトと作成するオブジェクトをそれぞれ分けたい場合に用いられる

### 目的
- 同じ作成過程で異なる表現形式の結果を得る
- サブクラスに応じて、作成されるクラスのインスタンスの中身を変える

### 構成要素
- Product: 作成されるオブジェクト
- Builder: Product を生成する処理を記述したインタフェース
- ConcreateBuilder: Builder の処理を具体化したクラス
- Director: Builder を利用するクラス

## Factory Method
### 概要
- 工場のように大量の製品を作成する
- インタフェースで処理の骨組みを作りサブクラスを用いてオブジェクトを作成する
- サブクラスに応じて、作成されるオブジェクトのタイプを変える
  
### 目的
- オブジェクトの生成とオブジェクトの具体的な処理を分離することで、柔軟にオブジェクトを利用でき再利用性を高める

### 構成要素
- Product: 作成するオブジェクトの構成要素を定義するインタフェース
- ConcreteProduct: Product を具体化したインタフェース
- Creator: Product を生成する処理を定義したインタフェース
- ConcreteCreator: Creator を具体化した ConcreteProduct を作成するクラス

## Abstract Factory
### 概要
- 関連する部品を組み合わせて製品を作成するとき
- 抽象的な工場、抽象的な部品を利用して、様々な製品を作成する
- 抽象クラスを継承した複数の部品を組み合わせて一つの製品を作成する
 
### 目的
- 複数の部品を組み合わせることで、様々な製品を作成する
- 抽象クラスを継承した部品を作成することで拡張性を高める

### 構成要素
- Product: 作成するオブジェクトの部品を定義するインタフェース
- ConcreteProduct: Product を具体化したクラス
- Factory: Product を生成する処理を定義したインタフェース
- ConcreteFactory: ConcreteProduct を作成する Factory を具体化したクラス

## Singleton
### 概要
- インスタンス作成時に同じオブジェクトが指定され、インスタンスが1つしか作成されないことを保証する

## Prototype
### 概要
- 原型や試作品の意味
- Prototype パターンは、あるインスタンスから同じクラスのインスタンスのクローンを作成するデザインパターン
- インタフェースで複製するオブジェクトの骨組みを作成する
- 複製したいクラスはインタフェースを継承する
- 複製したい状態でクラスを登録して、必要に応じて複製を作成する

### 目的
- あるインスタンスから同じインスンタンスのコピーを作成して、複製作業を簡単にできるようにする

### 構成要素
- Prototype: 複製するオブジェクトの構成要素を定義するインタフェース
- ConcretePrototype: Prototype を具体化したクラス
- Manager: ConcretePrototype を登録し、複製を作成するクラス

# 構造に関するパターン
## Adapter
### 概要
- コンセントのアダプターの意味
- 例えば、 iPhone に接続する用の端子を Android でも接続できるように iPhone の端子を Android に変換する
- Adapter につなぎちあクラスを作成する
- Adapter に処理を記述するためのインタフェースを作成する
- Adapter を作成して、 Adapter と接続できるようにする

### 目的
- クラスとクラスの間をつないで、型の違いを解消すること
  
### 構成要素
- Adaptee: Adapter に接続されるクラスを抽象化したインタフェース
- ConcreateAdaptee: Adaptee の処理を具体的に記述したクラス
- Adapter(Target): Adaptee を利用する処理を記載したインタフェース
- ConcreteAdapter: Adapter の処理を具体化したクラス

## Bridge
### 概要
- 各機能を構成している要素を抽象クラスでつないで、柔軟に機能追加を行う
- ある機能を持った Implementer と ConcreteImplementer を作成する Bridge を用いて、別のクラスにつなぎ新規の機能を追加する

### 目的
- 機能拡張が容易にできるようにして、拡張時に外のクラスに影響が出ないようにする

### 構成要素
- Implementer: 基本的な機能を記述したインタフェース
- ConcreteImplementer: Implementer を継承して処理を具体的に記述するクラス
- Abstraction: 追加として実装される機能を Implementer と切り離して作成する処理を記述した抽象クラス
- RefinedAbstraction: Abstraction の処理を具体的に記述したクラス

## Composite
### 概要
- 木と葉をもった階層構造をプログラム上で表現したい場合に用いられる
- どの節にどの葉を要素として追加していくのか把握することが難しい場合、Composite パターンを用いてツリー構造を表現する
- 葉と節のもつ共通の機能を持つ Component を作成して、Component を継承した Composite と Reaf を作成する
- Composite をインスンタンス化してその Composite の子要素とする Composite, Reaf を作成する
 
### 目的
- ツリー階層構造をわかりやすく表現する

### 構成要素
- Component: Composite と Reaf の共通機能を持った抽象クラス
- Composite: 容器を表す役を持ったクラスで、この中に Composite, Reaf を入れていき、階層構造を作成する
- Reaf: 中身を表す役のクラス。この中には要素を入れることができない

## Decorator
### 概要
- デコレーションとは飾り付けのことで、別のクラスの持っている特定の機能を別のクラスに追加するデザインパターン
- 互いに関連したクラスの処理をクラスをまたいで追加していきたい場合に用いる
- Component を継承した ConcreteComponent, Decorator を作成し、Decorator は Component をプロパティに持つ
- Decorator を継承した ConcreteDecorator を作成して、利用する際にプロパティに ConcreteComponent を設定する
 
### 目的
- 複数の機能を一つのクラスにまとめる

### 構成要素
- Component: 機能を追加する際の中核となるクラス
- ConcreteComponent: 追加する処理を記載した Component を継承したクラス
- Decorator: Component を継承したクラスで、プロパティに Component を持つ
- ConcreteDecorator: Decorator の処理を具体的に記述したクラス

## Facade
### 概要
- 建物の正面のこと
- 各クラスが関連しあって実行される複雑な処理を、Facadeが各クラスを利用してわかりやすくする
- システムを構成するクラスを作成する
- システムを構成するクラスを利用するための Facade を作成し、ユーザーに対するインタフェースを提供する

### 目的
- 複雑なシステムを扱うための、シンプルなインタフェースを提供すること

### 構成要素
- Facade: システムを構成する様々なクラスを利用するためのクラス
- その他のクラス: 色々な処理が記載された Facade に利用されるクラス

## Flyweight
### 概要
- オブジェクトを共有することで、メモリの使用量を少なくするために用いる
- Flyweight を作成する
- Flyweight をインスタンスとして所有する FlyweightFactory を作成する

### 構成要素
- Flyweight: 普通に用いるとメモリ使用量が大きいため、共有したほうがよいものを表す
- FlyweightFactory : Flyweight を作成する工場。FlyweightFactory を利用して Flyweight を作成するとオブジェクトが共有される

## Proxy
### 概要
- Proxy とは代理を表しており、あるオブジェクトの代わりに処理を行う
- オリジナルのオブジェクトへのアクセスをコントロールしたい場合に利用する
- インスタンス化する際に、時間がかかるとき
- 処理が複雑、危険な処理がありチェックをしたいとき
- Subject を継承した RealSubject に処理を記述する
- Subject を継承した Proxy を作成して RealSubject の代わりに処理を行う

### 目的
- 特定のオブジェクトに代わって処理を行う

### 構成要素
- Subject: RealSubject と Proxy を同一視して利用するためのインタフェース
- RealSubject: Subject を継承して処理を記述する
- Proxy: RealSubject の代わりにクライアントからの処理を返す。自分で処理ができなかった場合に RealSubject を呼び出す

# 振る舞いに関するパターン
## ChainOfResponsibility
### 概要
- 複数の処理をつなげて処理をしたい場合に使用する
  - 1.入力に対してXXか
  - 2.入力に対してXXか
  - 3.入力に対してXXか
- 別のクラスを繋げて処理できるような Handler を作成する
- Handler を継承した ConcreteHandler を作成して具体的な処理を実装し、インスンタンス化したのち各インスンタンスを繋いで処理を実行する

### 目的
- 複数の処理をつなげて、フィルター処理などを実装する

### 構成要素
- Handler: 要求を処理するインタフェース
- ConcreteHandler: Handler を具体化したもの。自分で処理ができる場合は処理し、処理できない場合は別のクラスに処理を回す

## Command
### 概要
- ソフトで、様々なボタンを持ったツールバーを作成する場合に、それぞれのボタンの処理を実装してツールバーに設定する
- ボタンを押した際の処理を execute メソッドとして親クラスで抽象化して、子クラスで実装し、各インスタンスをツールバーに設定して、ツールバーを作成する
- Receiver を作成する
- Command を継承して ConcreteCommand を作成し、それぞれ Receiver を扱えるようにする
- Invoker を作成して、 Command を設定して利用できるようにする

### 目的
- 複雑なコマンドを設定して利用できるようにし、コマンドの再利用性、拡張性を高めるように設計する

### 構成要素
- Command: 命令を定義したインタフェース
- ConcreteCommand: Command を具体化したもの。Receiver を扱った命令を記述する
- Receiver: Command が命令を実行する際の対象となるクラス
- Invoker: 命令の実行を開始する役目となるクラス
