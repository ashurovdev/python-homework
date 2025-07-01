import pandas as pd

data_excel = pd.read_excel('../data_json/titanic.xlsx')

print(data_excel.head(5))