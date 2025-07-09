import pandas as pd

titanic_df = pd.read_excel('../data/titanic.xlsx')

pipeline_df = (
    titanic_df[titanic_df['Survived'] == 1]
    .copy()
)

mean_age = pipeline_df['Age'].mean()
pipeline_df['Age'] = pipeline_df['Age'].fillna(mean_age)

pipeline_df['Fare_Per_Age'] = pipeline_df['Fare'] / pipeline_df['Age']

print(pipeline_df[['Survived', 'Age', 'Fare', 'Fare_Per_Age']].head())
