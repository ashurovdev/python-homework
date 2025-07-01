import pandas as pd

data_csv = pd.read_csv('../data/movie.csv')
movie2h = data_csv[data_csv['duration'] >= 200]
des_facebook_likes = data_csv.sort_values(by='director_facebook_likes', ascending=False)
print(movie2h)
print(des_facebook_likes)