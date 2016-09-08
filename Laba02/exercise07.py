import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.001)
y = np.cos(np.pi*x)

for n in range(30):
    y += 0.5**n * np.cos(3**n * np.pi * x)

plt.plot(x, y)
plt.title(r'Veyerstrasse')
plt.show()