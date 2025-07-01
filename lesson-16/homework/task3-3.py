import pandas as pd

data_csv = pd.read_csv('../data/movie.csv')

high_liked = data_csv.sort_values(by='director_facebook_likes', ascending=False)
print(high_liked.head(1))

longest_movies = data_csv.sort_values(by='duration', ascending=False).head(5)

for _, movie in longest_movies.iterrows():
    print(f'{movie["movie_title"]} - Directed by {movie["director_name"]}')
