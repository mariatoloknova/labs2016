n = int(input())
arr = list(map(int, input().split()))

MIN = min(arr)
Min = arr[0]

for i in range(n // 2):
    for x in arr:
        if x > MIN and x != MIN and x < Min:
            Min = x
    MIN = Min
    Min = arr[0]

print(MIN)