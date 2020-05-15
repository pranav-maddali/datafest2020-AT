Bonds <- read.table(file = "~/Desktop/Bonds 5.csv", header = TRUE, sep = ",")
Bonds <- matrix(c(411.2,83,494.2,732.1,102.2,834.3), ncol=2)
colnames(Bonds) <- c('YTD 2019', 'YTD 2020')
rownames(Bonds) <- c('Investment Grade', 'High Yield', 'Total')
Bonds.table <- as.table(Bonds)
Bonds

barplot(Bonds, main = "US Bonds Issuance", xlab = 'Time', ylab = 'Bonds issued (in millions)', beside=T, xpd = TRUE, col=c('dark blue','blue','light blue'))
legend("topleft", legend=c("Investment Grade", "High Yield", "Total"),
       col=c("dark blue", "blue", "light blue"), cex=0.5,
       title="Legend", text.font=4, fill = c("darkblue", "blue", "light blue"))

