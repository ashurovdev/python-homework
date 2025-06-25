import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=0, scale=1, size=1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

plt.title("Normal taqsimotli histogramma (mean=0, std=1)")
plt.xlabel("Qiymatlar")
plt.ylabel("Frekansiya (chiqishlar soni)")
plt.grid(True)

plt.show()
