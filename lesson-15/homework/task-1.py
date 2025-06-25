#  f(x) = x^2 - 4x + 4
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 6)
def f_x(x):
    return x**2 - 4*x + 4

y = f_x(x)

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y', rotation=0)
plt.legend()
plt.show()
