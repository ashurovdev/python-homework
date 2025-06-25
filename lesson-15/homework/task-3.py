import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import xlabel

x = np.linspace(-2, 2, 400)
x_pos = np.linspace(0, 2, 400)

fig, axs = plt.subplots(2,2, figsize = (10,8))

axs[0,0].plot(x, x**3, color = 'blue')
axs[0,0].set_title(r'$f(x) = x^3$')
axs[0,0].set_xlabel(r'$x$')
axs[0,0].set_ylabel(r'$f(x)$')
axs[0,0].grid(True)

axs[0,1].plot(x, np.sin(x), color = 'red')
axs[0,1].set_title(r'$f(x) = sin(x)$')
axs[0,1].set_xlabel(r'$x$')
axs[0,1].set_ylabel(r'$f(x)$')
axs[0,1].grid(True)

axs[1,0].plot(x, np.exp(x) , color = 'green')
axs[1,0].set_title(r'$f(x) = e^x$')
axs[1,0].set_xlabel(r'$x$')
axs[1,0].set_ylabel(r'$f(x)$')
axs[1,0].grid(True)

axs[1,1].plot(x, np.log(x_pos + 1), color = 'orange')
axs[1,1].set_title(r'$f(x) = log(x_pos + 1)$')
axs[1,1].set_xlabel(r'$x$')
axs[1,1].set_ylabel(r'$f(x)$')
axs[1,1].grid(True)

plt.tight_layout()
plt.show()