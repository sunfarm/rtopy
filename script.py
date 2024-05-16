import pandas as pd
import numpy as np

def rle_encode(data):
    data = np.array(data)
    n = len(data)
    if n == 0:
        return pd.DataFrame(columns=['Lengths', 'Values'])

    # Find where the data changes
    changes = np.concatenate(([True], data[1:] != data[:-1], [True]))
    indices = np.where(changes)[0]

    # Calculate lengths of runs
    lengths = np.diff(indices)
    values = data[indices[:-1]]  # Correct indexing to avoid out-of-bounds

    return pd.DataFrame({'Lengths': lengths, 'Values': values})

data = pd.read_csv('inputs.csv')
encoded_data = rle_encode(data['Category'])
encoded_data.to_csv('output_python.csv', index=False)
