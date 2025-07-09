import sqlite3
import pandas as pd

with sqlite3.connect('../data/chinook.db') as conn:
    customers = pd.read_sql('SELECT * FROM customers', con=conn)
    invoices = pd.read_sql('SELECT * FROM invoices', con=conn)

merged_df = pd.merge(customers, invoices, on='CustomerId', how='inner')

invoice_counts = merged_df.groupby(['CustomerId', 'FirstName', 'LastName']).size().reset_index(name='InvoiceCount')

print(invoice_counts)
