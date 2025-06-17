import numpy as np

m5 = np.random.random((5, 5))
row_sums = m5.sum(axis=1)
col_sums = m5.sum(axis=0)
print(row_sums)
print( col_sums)