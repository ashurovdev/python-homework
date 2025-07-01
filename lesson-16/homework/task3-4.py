import pandas as pd

df = pd.read_parquet('../data/flights')

print("Ustunlardagi yo\'qolgan qiymatlar soni: ")
print(df.isnull().sum())
if 'DepDelay' in df.columns:
    if df['DepDelay'].dtype != 'O':
        mean_value = df['DepDelay'].mean()
        df['DepDelay'].fillna(mean_value, inplace=True)
        print(f"\n'DepDelay' ustunidagi yo\'qolgan qiymatlar o\'rtacha ({round(mean_value, 2)}) bilan to\'ldirildi.")
    else:
        print("\n'DepDelay' ustuni raqamli emas.")
else:
    print("\n'DepDelay' ustuni topilmadi.")
