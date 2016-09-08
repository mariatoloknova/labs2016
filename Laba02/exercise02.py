import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-3, 0, 0.001)
y = x**2 - x - 6

plt.subplot(121)
plt.plot(x, y)
plt.subplot(121).spines['bottom'].set_position('center')
plt.subplot(121).spines['left'].set_position('center')
plt.grid(True)

x = np.arange(2, 4, 0.001)
y = x**2 - x - 6

plt.subplot(122)
plt.plot(x, y)
plt.subplot(122).spines['bottom'].set_position('center')
plt.subplot(122).spines['left'].set_position('center')
plt.grid(True)

plt.show()
