import pandas as pd

flights_df = pd.read_parquet('../data/flights')

pipeline_df = (
    flights_df[flights_df['DepDelay'] > 30].copy()
)

pipeline_df = pipeline_df.dropna(subset=['DepDelay', 'AirTime'])
pipeline_df = pipeline_df[pipeline_df['AirTime'] > 0]

pipeline_df['Delay_Per_Hour'] = pipeline_df['DepDelay'] / (pipeline_df['AirTime'] / 60)

print(pipeline_df[['DepDelay', 'AirTime', 'Delay_Per_Hour']].head(10))
