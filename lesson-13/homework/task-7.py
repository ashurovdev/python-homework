import numpy as np

mat_5x5 = np.random.random((5, 5))
norm_matrix = (mat_5x5 - mat_5x5.min()) / (mat_5x5.max() - mat_5x5.min()) 
print(norm_matrix)