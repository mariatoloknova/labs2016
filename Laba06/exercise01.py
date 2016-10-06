import random
import matplotlib.pyplot as plt

random.seed(0)
plt.subplot(221)
plt.hist([random.normalvariate(0, 1) for i in range(100)], bins = 100)
plt.title(r"N = 100")
plt.subplot(222)
plt.hist([random.normalvariate(0, 1) for i in range(1000)], bins = 100)
plt.title(r"N = 1000")
plt.subplot(223)
plt.hist([random.normalvariate(0, 1) for i in range(10000)], bins = 100)
plt.title(r"N = 10000")
plt.subplot(224)
plt.hist([random.normalvariate(0, 1) for i in range(100000)], bins = 100)
plt.title(r"N = 100000")
plt.show()