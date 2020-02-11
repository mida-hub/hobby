
# sample data

## データ呼び出し
data(iris)

## 構造確認
str(iris)

## 要約統計量
summary(iris)

## 行数
nrow(iris)

## 列数
ncol(iris)

## カラム名
colnames(iris)

## 行数指定表示
iris[c(1, 4), ]

### 複数行表示
iris[1:4,]

## 列数指定表示
iris[, c(1, 4)]

iris$Species

## 量的変数
as.factor(iris$Petal.Width)

## 質的変数
as.integer(iris$Species)
