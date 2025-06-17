import numpy as np

A = np.random.random((3, 3))
b = np.random.random(3)
x = np.linalg.solve(A, b)
print(x)