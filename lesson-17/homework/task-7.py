import pandas as pd

employees_df = pd.read_csv('../data/employee.csv')
employees_df.columns = employees_df.columns.str.lower()

def normalize_salary(group):
    min_salary = group['base_salary'].min()
    max_salary = group['base_salary'].max()
    group['normalized_salary'] = (group['base_salary'] - min_salary) / (max_salary - min_salary)
    return group


normalized_df = employees_df.groupby('department', group_keys=False).apply(normalize_salary).reset_index(drop=True)


print(normalized_df[['department', 'base_salary', 'normalized_salary']].head(10))
