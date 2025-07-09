import pandas as pd

def Age_Group(age):
    if pd.isna(age):
        return 'Unknown'
    elif age < 18:
        return 'Child'
    else:
        return 'Adult'
titanic_df = pd.read_excel('../data/titanic.xlsx')
titanic_df['Age_Group'] = titanic_df['Age'].apply(Age_Group)
print(titanic_df)