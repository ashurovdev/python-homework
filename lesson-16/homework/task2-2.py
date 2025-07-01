import pandas as pd
from collections import Counter

data_excel = pd.read_excel('../data/titanic.xlsx')
age_list = data_excel[data_excel['Age'] > 30]
gender_list = Counter(data_excel['Sex'])
print(age_list)
print(gender_list)