import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_percentile(values, bucket_number):
    step = 100 / bucket_number
    return [np.percentile(values, i*step) for i in range(bucket_number)]

def get_percentile_number(value, percentiles):
    i = 0
    while value >= percentiles[i]:
        i += 1
        if i == len(percentiles):
            break
    if i > 0:
        return i - 1
    else:
        return i

def value_equalization(value, percentiles, add_random=False):
    step = 1/len(percentiles)
    idx = get_percentile_number(value, percentiles)
    if add_random:
        return idx * step + random.uniform(0, step)
    else:
        return idx * step

def values_equalization(values, percentiles, add_random=False):
    return [value_equalization(value, percentiles, add_random = add_random) for value in values]

random.seed(0)
#Считываем данные в массив numpy
data = pd.read_csv("img.txt", sep = " ", header = None)
data = np.array(data)
#Создаём рандомные 100 строчек различными способами
top100 = random.choice(data)
random100 = np.array(random.sample(list(data), 100))
for i in range(99):
    top100 = np.vstack([top100, random.choice(data)])
#Создаём графики строчек
plt.subplot(321)
plt.imshow(top100, cmap = plt.get_cmap('gray'))
plt.subplot(322)
plt.imshow(random100, cmap = plt.get_cmap('gray'))
#Создаём графики необработанных данных
plt.subplot(323)
plt.imshow(data, cmap = plt.get_cmap('gray'))
plt.subplot(324)
plt.hist(data.flatten())
#Эквализируем данные
# for i in range(len(data)):
#     percentiles = get_percentile(data[i], 4)
#     if min(data[i]) > 0: #Ставим в начало 0, если все числа положительные
#         percentiles[0] = 0.0
#     data[i] = values_equalization(data[i], percentiles[1:], add_random = True)
percentiles = get_percentile(data.ravel(), 4)
percentiles[0] = 0.0
for i in range(len(data)):
    data[i] = values_equalization(data[i], percentiles, add_random=True)
print(data)
plt.subplot(325)
plt.imshow(data[130:140, 110:120], cmap = plt.get_cmap('gray'))
plt.subplot(326)
plt.hist(data.flatten()) #По гистограмме у меня вроде всё норм
plt.show()

data = data.flatten()
print(data.mean())