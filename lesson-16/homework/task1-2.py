import pandas as pd

data_json = pd.read_json('../data/iris.json')

print(data_json.shape)
print(data_json.columns.tolist())