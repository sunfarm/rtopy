# Load the data from CSV file
data <- read.csv("inputs.csv")

# Fit a linear model
model <- lm(scores ~ hours, data=data)

# Print the summary of the model
summary(model)

# Make predictions using the fitted model
predictions <- predict(model, data)

# Round predictions to 3 significant digits
rounded_predictions <- signif(predictions, digits=6)

# Create a new data frame with the original data and the rounded predictions
output_data <- data.frame(hours=data$hours, scores=data$scores, predicted_scores=rounded_predictions)

# Write the output data to a CSV file
write.csv(output_data, "output_r.csv", row.names=FALSE)
