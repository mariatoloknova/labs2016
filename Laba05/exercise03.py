A = [1,2,3,4,5]
#A = [1,2,3,4]

for i in range(1, len(A)//2+1):
    A[i], A[-1] = A[-1], A[i]
print(A)