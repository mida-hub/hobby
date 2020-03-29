# sim1
n_group <- 15
n_obs <- 20

set.seed(1)
value <- rnorm(n_group*n_obs)
group <- as.factor(rep(1:n_group, each=n_obs))

df_sim1 <- data.frame(group, value)

str(df_sim1)
summary(df_sim1)

with(df_sim1, boxplot(value ~ group))
with(df_sim1, by(value, INDICES=group, FUN=mean))
with(df_sim1, by(value, INDICES=group, FUN=var))

res <- with(df_sim1, pairwise.t.test(value, group, p.adjust.method="none"))
res
sum(res$p.value<0.05, na.rm=TRUE)

res_adj <- with(df_sim1, pairwise.t.test(value, group), p.adjust.methods="bonferroni")
res_adj
sum(res_adj$p.value<0.05, na.rm=TRUE)

#sim2
