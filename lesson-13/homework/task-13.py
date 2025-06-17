import numpy as np

mat_3x3 = np.random.random((3, 3))
vec_3 = np.random.random(3)
mat_vec = np.dot(mat_3x3, vec_3)
print(mat_vec)