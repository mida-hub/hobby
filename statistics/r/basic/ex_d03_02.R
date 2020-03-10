# anova

root_dir <- getwd()
csvPATH <- "./data/Benefit.csv"

# plot データ確認
plot(iris[, 1:4])
plot(iris[, 1:4], col=as.numeric(iris$Species))

par(mfrow=c(2, 2))
  with(iris, hist(Sepal.Length))
  with(iris, hist(Sepal.Width))
  with(iris, hist(Petal.Length))
  with(iris, hist(Petal.Width))
par(mfrow=c(1, 1))

par(mfrow=c(2, 2))
  with(iris, boxplot(Sepal.Length~Species, main="Sepal.Length"))
  with(iris, boxplot(Sepal.Width~Species, main="Sepal.Width"))
  with(iris, boxplot(Petal.Length~Species, main="Petal.Length"))
  with(iris, boxplot(Petal.Width~Species, main="Petal.Width"))
par(mfrow=c(1, 1))

with(iris, by(Sepal.Width, INDICES=Species, FUN=mean))
with(iris, by(Sepal.Width, INDICES=Species, FUN=var))

# 分散分析 平均に差はないを棄却
anova(lm(Sepal.Width ~ Species, data=iris))

anova(aov(Sepal.Width ~ Species, data=iris))

oneway.test(Sepal.Width ~ Species, data=iris, var.equal=TRUE)

# 3変数
with(iris, pairwise.t.test(Sepal.Width, Species, p.adjust.method = "none"))

with(iris, pairwise.t.test(Petal.Length, Species, p.adjust.method = "none"))
