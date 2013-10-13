require(ggplot2)
data<-read.csv("comb", header=F)
colnames(data) <- c("a","b")
qplot(data$b, binwidth=.5) + xlab("Substitution Rate") + ylab("Frequency")