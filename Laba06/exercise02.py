import random
import matplotlib.pyplot as plt

def func(x):
    if -2 <= x <= 2:
        return -x**2 + 4
    else:
        return 0

N = int(input())
x = [random.uniform(-3,3) for i in range(N)]
y = [func(x[i]) for i in range(N)]
print( (6/N) * sum(y) )