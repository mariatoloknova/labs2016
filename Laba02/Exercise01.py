import math
def func(x):
    a = math.exp(1/(math.sin(x)+1))
    b = (5/4+1/(x**15))
    return math.log(a/b, 1+x**2)
print(func(1))
print(func(10))
print(func(1000))