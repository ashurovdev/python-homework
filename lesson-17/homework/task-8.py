import pandas as pd

movies_df = pd.read_csv('../data/movie.csv')

def Duration(dur):
    if pd.isna(dur):
        return 'Unknown'
    elif dur < 60:
        return 'Short'
    elif dur >= 60 and dur < 120:
        return 'Medium'
    else:
        return 'Long'

movies_df['duration_sort'] = movies_df['duration'].apply(Duration)

print(movies_df.head())
