import pandas as pd
import numpy as np

data_json = pd.read_json('../data/iris.json')

columns = ['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth']

for col in columns:
    mean = np.mean(data_json[col])
    median = np.median(data_json[col])
    std = np.std(data_json[col])
    print(f'{col}:\n  Mean: {mean:.2f} \n  Median: {median:.2f} \n  Standard Deviation: {std:.2f}\n')
