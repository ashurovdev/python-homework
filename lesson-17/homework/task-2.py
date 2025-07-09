import pandas as pd

df1 = pd.read_csv('../data/movie.csv')[['director_name', 'color']]

df2 = pd.read_csv('../data/movie.csv')[['director_name', 'num_critic_for_reviews']]

merged_df_left = pd.merge(df1, df2, on='director_name', how='left')

merged_df_outer = pd.merge(merged_df_left, df2, on='director_name', how='outer')

print(f'Left: {len(merged_df_left)}\n\n{merged_df_left}')
print(f'Outer: {len(merged_df_outer)}\n\n{merged_df_outer}')