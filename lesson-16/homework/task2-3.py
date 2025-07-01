import pandas as pd

df = pd.read_parquet('../data/flights', columns=['Origin', 'Dest', 'Reporting_Airline'])

print(df.head())

unique_dests = df['Dest'].nunique()
print(f"Number of unique destinations: {unique_dests}")
