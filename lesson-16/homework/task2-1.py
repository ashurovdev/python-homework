import pandas as pd

data_json = pd.read_json('../data/iris.json')
data_json.columns = data_json.columns.str.lower()
print(data_json[['sepallength', 'sepalwidth']])