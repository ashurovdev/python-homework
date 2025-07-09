import pandas as pd

movie_df = pd.read_csv('../data/movie.csv')
grouped = movie_df.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews':'sum',
    'duration':'mean'
})

print(grouped)