import numpy as np
import matplotlib.pyplot as plt

def func(x):
    a = (x**2 + 1)*np.exp(-np.abs(x)/10)
    b = (1+np.tan(1/(1+np.sin(x)**2)))
    return a/b

x = np.arange(-20, 20, 0.01)
y = func(x)

plt.plot(x, y)
plt.show()