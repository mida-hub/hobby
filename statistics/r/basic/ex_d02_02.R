# d: density => 確率密度
# p: probability => 下側確率の値に対する,分位点 . ( = 確率変数 Xに対し P(X < 値) = ? を返す)
# q: quantile => 分位点に対する、値(e.g. Z値) . pとq は表裏一体. Quantile( P(X < 値)) = 値 
# r: random => 乱数生成

# normal distribution
# dnorm

dnorm(0, mean=0, sd=1)

x <- seq(-4, 4, by=0.05)

plot(x,
     dnorm(x, mean=0, sd=1),
     main="Standard Normal Distribution",
     xlab="x",
     ylab="f(x)"
     )

plot(x,
     dnorm(x, mean=0, sd=1),
     type="l",
     main="Standard Normal Distribution, alpha=0.05",
     xlab="x",
     ylab="f(x)"
)

xval <- seq(-4, -1.96, by=0.04)
xvals <- c(xval, rev(xval))
xvals <- c(xvals, -1 * xvals)

yvals <- c(rep(0, length(xval)), dnorm(rev(xval), mean=0, sd=1))
yvals <- c(yvals, rev(yvals))
polygon(xvals, yvals, col="gray")

abline(v= 1.96, col="red", lwd=2, lty=2)
abline(v=-1.96, col="red", lwd=2, lty=2)
text(-1.96,  0.3,   "-1.96", col="red",  pos=2)
text( 1.96,  0.3,    "1.96", col="red",  pos=4)
text(-1.96, 0.05,   "0.25%", col="blue", pos=2)
text( 1.96, 0.05, "1-0.975", col="blue", pos=4)

# Quantile
plot(x,
     dnorm(x, mean=0, sd=1),
     type="l",
     xlab="x",
     ylab="f(x)",
     main="Standard Normal Disrtibution, Quantile 0.975"
     )
xval <- seq(-4, 1.96, by= 0.04 )
xvals <- c(xval, rev(xval))
yvals <- c(rep(0, length(xval)), dnorm(rev(xval), mean=0, sd=1))
polygon(xvals, yvals, col="gray")

abline(v=1.96, col="red", lwd=2, lty=2)
text(1.96, 0.3, "1.96", col="red", pos=4)
text(0, 0.2, "97.5%", col="blue")

## p: probability
pnorm(1.96)  # 0.975 

## q: quantile
qnorm(0.975)  # 1.959964


