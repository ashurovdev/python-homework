import pandas as pd

flights_df = pd.read_parquet('../data/flights')
grouped = flights_df.groupby(['Year', 'Month']).agg({
    'ArrDelay':'mean',
    'DepDelay':'sum',
    'FlightNum':'count',
})

print(grouped)