import pandas as pd

# Read data
data = pd.read_csv('inputs.csv')

# Transformation (Example: calculate the mean of 'Values')
mean_values = data['Values'].mean()

# Save output
data_out = pd.DataFrame({'Mean': [mean_values]})
data_out.to_csv('output_python.csv', index=False)
