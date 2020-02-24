mcs_and_plot_function <- function(N){
  set.seed(12345)
  # 円を描く
  # x^2 + y^2 = 1
  # y = sqrt(1 - x^2)
  x = seq(0, 1, by=0.001)
  y = sqrt(1 - x^2)

  # 乱数を発生させる
  xmc = runif(N, 0, 1)
  ymc = runif(N, 0, 1)
  
  # 円の範囲内か
  threshold  = (xmc^2 + ymc^2) <= 1
  # color用
  threshold_factor = as.factor(threshold)

  # 円の描画
  plot(x, y, type="l", xlim=c(0, 1), ylim=c(0, 1))
  # plotを重ねる
  par(new=T)
  # 乱数を描画
  # cexは点の大きさ
  plot(xmc, ymc, col=threshold_factor, xlim=c(0, 1), ylim=c(0, 1), cex=0.1)

  # 円の面積
  true_value = pi / 4
  # モンテカルロ法
  mcs = sum(threshold) / N
  
  print(true_value)
  print(mcs)
}

mcs_and_plot_function(100)
mcs_and_plot_function(1000)
mcs_and_plot_function(10000)

mcs_ratio_function <- function(N){
  set.seed(12345)        
  mcs_ratio <- c(NULL)
  # 乱数を発生させる
  xmc = runif(N, 0, 1)
  ymc = runif(N, 0, 1)
  # 円の範囲内か
  threshold  = (xmc^2 + ymc^2) <= 1
  for(i in 1:N){
    mcs = sum(threshold[1:i]) / i
    mcs_ratio = c(mcs_ratio, mcs)
  }
  # 描画
  plot(seq(1, N), mcs_ratio, type="l")
  abline(h=(pi / 4), col='red', lty=2)
}
mcs_ratio_function(3000)
