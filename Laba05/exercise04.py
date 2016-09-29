k = list(map(int, input().split()))
t = int(input())
for i in range(t):
    k = k[:-k[-1]-1] + k[-1:] + k[-k[-1]-1:-1]
print(k)