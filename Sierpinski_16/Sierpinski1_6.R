library("spt")
t= st(60, 60)
setwd("")
for (i in 1:6) {
  jpeg(file=paste(paste("sierpinski", i, sep = " "),"jpeg", sep="."))
  plot(t, iter=i, main=paste("Iteration", i, sep=" "))
  dev.off()

}

  

plot(t, iter=1, main=paste("Iteration", 1, sep=" "))