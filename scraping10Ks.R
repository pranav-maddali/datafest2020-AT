library(finreportr)
library(gmp)
vec_assets <- numeric(10)
vec_liabilities <- numeric(10)
vec_names <- vector(, length = 10)
i <- 1
###program to scrape 10Ks based off of ticker and year given
repeat{
  strname <- readline("Enter the ticker for the company or halt to terminate: ")
  if(tolower(strname) == "halt")
    break
  else
    vec_names[i] <- strname
  yrBR <- readline("Enter the year the company went bankrupt or 0 to terminate: ")
  if(yrBR == 0)
    break
  gbs <- GetBalanceSheet(strname, yrBR)
  counter_a <- 0
  ###store total assets
  for(row in 1:nrow(gbs)){
    if(gbs[row,1] == "Assets, Current"){
      amount <- gbs[row,3]
      if(counter_a == 1){
        vec_assets[i] <- amount
        break
      }
      counter_a <- 1
    }
  }
  counter_l <- 0
  ###store total liabilities
  for(row in 1:nrow(gbs)){
    if(gbs[row,1] == "Liabilities, Current"){
      amount <- gbs[row,3]
      if(counter_l == 1){
        vec_liabilities[i] <- amount
        break
      }
      counter_l <- 1
    }
  }
  i <- i + 1
  ###continuous resizing of vectors
  if(length(vec_names) <= i){
    vec_names <- c(vec_names, numeric(10))
    vec_assets <- c(vec_assets, numeric(10))
    vec_liabilities <- c(vec_liabilities, numeric(10))
  }
}
i <- i - 1

vec_names <- vec_names[seq_len(i)]
vec_assets <- vec_assets[seq_len(i)]
vec_liabilities <- vec_liabilities[seq_len(i)]

vec_assets <- as.bigz(vec_assets)
vec_liabilities <- as.bigz(vec_liabilities)


###calculating debt capacity
vec_debt <- vector(mode='raw', length = i)
counter <- 1

for(asset in i){
  vec_debt[counter] <- (vec_assets[counter])/(vec_liabilities[counter])
  counter <- counter + 1
}

###creating a data frame to present data of companies
df <- data.frame(
  df_name = vec_names,
  df_assets = vec_assets,
  df_liabilities = vec_liabilities,
  df_debt = vec_debt,
  stringsAsFactors = FALSE,
)
