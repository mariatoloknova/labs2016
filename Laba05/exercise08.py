n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

t = int(input())
i = 0

for x in arr:
    if x[0] <= t <= x[1]:
        i += 1

print(i)