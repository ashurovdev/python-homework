import sqlite3
import pandas as pd

with sqlite3.connect('../data/chinook.db') as conn:
    customers_table = pd.read_sql(
        '''SELECT * FROM customers''',
        con = conn)

print(customers_table.head(10))