k = int(input())
n = int(input())
A = []

for i in range(k):
    A.append(1)
for i in range(k, n+1):
    A.append(sum(A[i-k:i]))
    print(A)
print(A[-1])