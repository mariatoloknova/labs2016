n = int(input())
a = [i**2 for i in range(n) if i%3 == 1]
print(sum(a))