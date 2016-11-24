def fib(n):
    if (n == 1 or n == 2) and n > 0:
        return 1
    elif n <= 0:
        return "Not today!"
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input())
print(fib(n))
