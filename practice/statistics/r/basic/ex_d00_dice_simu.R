# ダイスシミュレーション
dice_function <- function(n){
  dice <- as.integer(runif(n, 1, 7))
  dice.table <- table(dice)
  print(dice.table)
  print(prop.table(dice.table))
  hist(dice,
       breaks=c(0, 1, 2, 3, 4, 5, 6),
       probability=T,
       main="Histogram of 1-6",
       xlab="dice",
       col="gray")
}

dice_function(100)
dice_function(1000)
dice_function(10000)
dice_function(100000)

dice_function2 <- function(n){
  dice <- sample(6, n, replace=TRUE)
  dice.table <- table(dice)
  print(dice.table)
  print(prop.table(dice.table))
  barplot(prop.table(dice.table),
          main="Barplot of 1-6",
          xlab="dice",
          ylab="probability",
          col="gray")
}

dice_function2(100)
dice_function2(1000)
dice_function2(10000)
dice_function2(100000)

# 中心極限定理
dice_mean_function <- function(n){
  dice.mean <- c(NULL)
  for (i in 1:n){
    dice <- as.integer(runif(100, 1, 7))
    dice.mean <- c(dice.mean, mean(dice))
  }
  dice.mean.table <- table(dice.mean)
  print(mean(dice.mean))
  print(var(dice.mean))
  print(sd(dice.mean))
  barplot(dice.mean.table)
}

dice_mean_function(100)
dice_mean_function(1000)
dice_mean_function(10000)
dice_mean_function(100000)

dice_mean_function2 <- function(n){
  dice <- matrix(sample(6, n * 100, replace=TRUE), n)
  dice.mean <- rowMeans(dice)
  dice.mean.table <- table(dice.mean)
  print(mean(dice.mean))
  print(var(dice.mean))
  print(sd(dice.mean))
  barplot(dice.mean.table)
}

dice_mean_function2(100)
dice_mean_function2(1000)
dice_mean_function2(10000)
dice_mean_function2(100000)
