data(iris)

# 描画 2 * 2
par(mfrow=c(2, 2))

# histogram
hist(iris$Sepal.Length)
hist(iris$Sepal.Width)
hist(iris$Petal.Length)
hist(iris$Petal.Length)

# mean
mean_sepal_length <- mean(iris$Sepal.Length)
mean_sepal_width  <- mean(iris$Sepal.Width)
mean_petal_length <- mean(iris$Petal.Length)
mean_petal_width  <- mean(iris$Petal.Length)

data.frame(mean_sepal_length,
           mean_sepal_width,
           mean_petal_length,
           mean_petal_width)

# sd
sd_sepal_length <- sd(iris$Sepal.Length)
sd_sepal_width  <- sd(iris$Sepal.Width)
sd_petal_length <- sd(iris$Petal.Length)
sd_petal_width  <- sd(iris$Petal.Length)

data.frame(sd_sepal_length,
           sd_sepal_width,
           sd_petal_length,
           sd_petal_width)

summary(iris)

# quantile
(10:0)/10
q_sepal_length <- quantile(iris$Sepal.Length, probs=(10:0)/10)
q_sepal_width  <- quantile(iris$Sepal.Width, probs=(10:0)/10)
q_petal_length <- quantile(iris$Petal.Length, probs=(10:0)/10)
q_petal_width  <- quantile(iris$Petal.Length, probs=(10:0)/10)

data.frame(q_sepal_length,
           q_sepal_width,
           q_petal_length,
           q_petal_width)

qtl <- data.frame(q_sepal_length,
                  q_sepal_width,
                  q_petal_length,
                  q_petal_width)

qtl
qtl[1]

rownames(qtl)[1]  <- "Max"
rownames(qtl)[6]  <- "Median"
rownames(qtl)[11] <- "Min"

qtl

# median
median(iris$Sepal.Length)

# 度数
ti <- table(iris$Species)
ti

# 相対度数
pi <- prop.table(table(iris$Species))
pi


# plot
barplot(ti)
barplot(pi)

pairs(iris)
pairs(iris, col=iris$Species)
plot(iris, col=iris$Species)

hist(iris$Sepal.Length)
hist(iris$Sepal.Width)

boxplot(iris)

