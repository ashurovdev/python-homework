import pandas as pd

data_excel = pd.read_excel('../data/titanic.xlsx')

max_age = data_excel['Age'].max()
min_age = data_excel['Age'].min()
age_sum = data_excel['Age'].sum()

print(max_age, min_age, age_sum)
