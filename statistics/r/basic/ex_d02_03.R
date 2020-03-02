## est

set.seed(12345)

population <- rnorm(n=20000, mean=300000, sd=600000)

length(population)
mean(population)
sd(population)

N <- 10
set.seed(12345)
sample10 <- sample(population, size=N, replace=FALSE)
mean(sample10)
sd(sample10)

s.e <- sd(sample10) / sqrt(length(sample10))
s.e

q.t <- qt(c(0.05/2, 1-0.05/2), df=N-1)
q.t

mean(sample10) + s.e * q.t

t.test(sample10)

sample_function <- function(p_population, N){
  set.seed(12345)
  sampleN <- sample(p_population, size=N, replace=FALSE)
  print(mean(sampleN))
  print(sd(sampleN))
  print(t.test(sampleN))
}

sample_function(population, 100)
sample_function(population, 1000)
sample_function(population, 10000)
sample_function(population, 15000)

## test

sales_a <- c(1000, 980, 1200, 1260, 1500, 1005, 820, 1490, 1500, 960)
sales_b <- c(880, 1080, 1580, 2180, 1900, 1950, 1200, 910, 2100, 1890)
t.test(sales_a, sales_b)

for(i in 9:15){
  res <- c(5, i)
  pop <- c(50, 50)
  print("-------------------")
  print(i)
  print(prop.test(res, pop))
  print("-------------------")
}



N_group <- 20

N_sim <- 1000  # シミュレーション回数。N_sim回の検定を実行
p_val <- c()
for(i in 1:N_sim){
        A <- rnorm(N_group, 30, 10)
        B <- rnorm(N_group, 35, 10)
        ttest <- t.test(A, B)
        p_val <- append(p_val, ttest$p.val)
}

mean(p_val)   # p値の平均
sum(p_val<=0.05) / N_sim   # N_sim中、p値が0.05を下回った割合



N_group <- 20

N_sim <- 1000  # シミュレーション回数。N_sim回の検定を実行
p_val <- c()
for(i in 1:N_sim){
        A <- rnorm(N_group, 30, 10)
        B <- rnorm(N_group, 30, 10)
        ttest <- t.test(A, B)
        p_val <- append(p_val, ttest$p.val)
}

mean(p_val)   # p値の平均
sum(p_val<=0.05) / N_sim   # N_sim中、p値が0.05を下回った割合
