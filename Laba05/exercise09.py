n = int(input())
arr = list(map(int, input().split()))
t = int(input())

MAX = sum(arr[:t])

for i in range(1, n-t):
    if sum(arr[i:i+t]) > MAX:
        MAX = sum(arr[i:i+t])

print(MAX)