import pandas as pd

titanic_df = pd.read_excel('../data/titanic.xlsx')
grouped = titanic_df.groupby('Pclass').agg({
    'Age':'mean',
    'Fare':'sum',
    'PassengerId': 'count'
})


print(grouped)