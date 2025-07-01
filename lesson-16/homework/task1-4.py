import pandas as pd

data_parquet = pd.read_parquet('../data/flights')

print(data_parquet.info())
