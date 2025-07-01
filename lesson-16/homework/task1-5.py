import pandas as pd

data_csv = pd.read_csv('../data/movie.csv')

print(data_csv.sample(10))