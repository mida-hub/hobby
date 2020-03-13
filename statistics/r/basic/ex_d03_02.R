root_dir <- getwd()
root_dir
csvPATH <- "./data/Benefit.csv"

benefit <- read.csv(file=csvPATH, header=T)

str(benefit)
summary(benefit)

hist(benefit$Satisfaction)

par(mfrow=c(1, 2))
  with(benefit, boxplot(Satisfaction ~ Benefit))
  with(benefit, boxplot(Satisfaction ~ Age))
par(mfrow=c(1, 1))  

model1 <- lm(Satisfaction ~ Benefit, data=benefit)
anova(model1)

model2 <- lm(Satisfaction ~ Benefit + Age, data=benefit)
anova(model2)

# 交互作用
model3 <- lm(Satisfaction ~ Benefit + Age + Benefit * Age, data=benefit)
anova(model3)

## 交互作用プロット
interaction.plot(benefit$Benefit, benefit$Age, benefit$Satisfaction)
interaction.plot(benefit$Age, benefit$Benefit, benefit$Satisfaction)

summary(model1)$r.squared
summary(model2)$r.squared
summary(model3)$r.squared

AIC(model1)
AIC(model2)
AIC(model3)
