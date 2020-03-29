# basket

root_dir <- getwd()
csvPATH1 <- "./data/Basket_en2.csv"

library(arules)

trans_dat <- read.transactions(csvPATH1, sep=",")
class(trans_dat)

as(trans_dat, "matrix")
as(trans_dat, "data.frame")
summary(trans_dat)

itemFrequencyPlot(trans_dat, type="absolute")

res <- apriori(trans_dat, parameter=list(minlen=2, maxlen=3, support=0.2, confidence=0))

inspect(res)
