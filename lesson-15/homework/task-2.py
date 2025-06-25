import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label='sin(x)', color = 'red', linestyle='--', marker='o')
plt.plot(x, y_cos, label='cos(X)', color = 'blue', linestyle='--', marker='o')

plt.title('sin(x) and cos(X)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()