import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import csv

def round_half_to_even(value):
    """Round half to even (banker's rounding)."""
    if (value - np.floor(value)) == 0.5:
        return np.floor(value / 2.0 + 0.5) * 2.0
    else:
        return np.round(value)

def signif(x, digits):
    """Round to a specified number of significant digits using banker's rounding."""
    if x == 0:
        return 0
    shift = 10 ** (digits - int(np.floor(np.log10(abs(x)))) - 1)
    shifted = x * shift
    rounded = round_half_to_even(shifted)
    return rounded / shift

# Load the data from CSV file
data = pd.read_csv("inputs.csv")

# Prepare the input and output variables
x = data[['hours']]
y = data['scores']

# Fit a linear model
model = LinearRegression()
model.fit(x, y)

# Make predictions using the fitted model
predictions = model.predict(x)

# Create a new DataFrame with the original data and the predictions
output_data = data.copy()
output_data['predicted_scores'] = predictions

# Write the output data to a CSV file
output_data['predicted_scores'] = output_data['predicted_scores'].apply(lambda x: signif(x, 6))
output_data.to_csv("output_python.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)
