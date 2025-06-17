import numpy as np

A = np.random.random((3, 4))
B = np.random.random((4, 3))
prod_matrix = np.dot(A, B)
print(prod_matrix)