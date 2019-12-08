library(AER)

N <- 200
sims <- 500
P <- 1
out <- matrix(NA, sims, P)
#X <- cbind(1, matrix(rnorm(N*(P-1)), N, P-1))
Markets <- 50



demand <- function(alpha, delta, price, demand_shock) {
  if(delta > 0) {
    stop("Demand curves slope downward, sorry AOC")
  }
  alpha + delta * price + demand_shock
}
supply <- function(gamma, psi, price, supply_shock) {
  if(psi < 0) {
    stop("Supply curves slope downward, sorry el presidente")
  }
  gamma + psi * price + supply_shock
}



for (s in 1:sims) {
  
  alpha <- rnorm(1, 15, 2)
  delta <- -exp(rnorm(1, 0, 1))
  gamma <- rnorm(1, -2, 1)
  psi <- exp(rnorm(1, 0, 1))
  xi_d <- rnorm(Markets)
  xi_s <- rnorm(Markets)
  supply_instrument <- xi_s + rnorm(Markets)
  prices <- rep(0, Markets)
  
  
  while(sum(abs(demand(alpha, delta, prices, xi_d) - 
                supply(gamma, psi, prices, xi_s))) > 0.01) {
    prices <- prices + 0.1*(demand(alpha, delta, prices, xi_d) - 
                              supply(gamma, psi, prices, xi_s))
    q_d <- demand(alpha, delta, prices, xi_d)
  }
  
  fit = ivreg(q_d ~ prices | supply_instrument , data = )
  delta_est <- coef(fit)[2]
  vcov_est <- sqrt(vcov(fit)[2,2])
  
  d <- rnorm(2000, delta_est, vcov_est)
  
  for(p in 1:length(d)) {
    out[p] <- mean(d[p] <= delta[p])
  }
  
  
}


#deltahat <- rnorm(P, 0, 2)
#sigmahat <- exp(rnorm(1))
#yhat <- rnorm(N, X %*% deltahat, sigmahat)

#Fit instrumental var model with
#Doing sbc on delta estimate


hist(as.vector(out))
plot.function(ecdf(out))
plot.function(punif, col = 2, add = T, type = "l")
ks.test(out, punif)



