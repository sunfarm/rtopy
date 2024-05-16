library(readr)

rle_encode <- function(data) {
  rle_data <- rle(data)
  lengths <- rle_data$lengths
  values <- rle_data$values
  return(data.frame(Lengths = lengths, Values = values))
}

data <- read_csv("inputs.csv")
encoded_data <- rle_encode(data$Category)
write_csv(encoded_data, "output_r.csv")
