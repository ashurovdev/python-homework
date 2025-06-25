import matplotlib.pyplot as plt
import numpy as np


x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)


colors = np.random.rand(100)

markers = ['o', '^', 's', 'D', '*']

plt.figure(figsize=(8, 6))

for i in range(100):
    marker = markers[i % len(markers)]
    plt.scatter(x[i], y[i], c=[[colors[i], colors[i], 1.0]], marker=marker, s=60)

plt.title("100 ta tasodifiy nuqta")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)

plt.show()
