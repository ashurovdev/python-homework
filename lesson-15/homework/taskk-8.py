import matplotlib.pyplot as plt
import numpy as np

time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [50, 40, 70, 60]
category_B = [30, 60, 50, 40]
category_C = [20, 30, 40, 50]

x = np.arange(len(time_periods))

plt.figure(figsize=(8, 6))
plt.bar(x, category_A, label='Category A', color='skyblue')
plt.bar(x, category_B, bottom=category_A, label='Category B', color='salmon')
plt.bar(x, category_C, bottom=np.array(category_A)+np.array(category_B), label='Category C', color='lightgreen')

plt.xticks(x, time_periods)
plt.xlabel("Vaqt oralig‘i")
plt.ylabel("Qiymat")
plt.title("Kategoriyalar bo‘yicha ustma-ust bar chart")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.show()
