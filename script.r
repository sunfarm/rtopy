library(readr)

# Read data
data <- read_csv("inputs.csv")

# Transformation (Example: calculate the mean of 'Values')
mean_values <- mean(data$Values)

# Save output
write_csv(data.frame(Mean=mean_values), "output_r.csv")
