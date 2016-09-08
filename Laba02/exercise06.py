import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 1.42, 1.76, 2, 2.24, 2.5]

p1, v1 = np.polyfit(x, y, deg=1, cov=True)
p_f1 = np.poly1d(p1)
print(p_f1)

p2, v2 = np.polyfit(x, y, deg=2, cov=True)
p_f2 = np.poly1d(p2)
print(p_f2)

plt.subplot(121)
plt.plot(x, p_f1(x))
plt.errorbar(x, y, xerr=v1[0][0], yerr=v1[1][1])
plt.grid()

plt.subplot(122)
plt.plot(x, p_f2(x))
plt.errorbar(x, y, xerr=v2[0][0], yerr=v2[1][1])
plt.grid()

plt.show()
