A = [1,2,3,4,5]

for i in range(len(A)-2, 0, -2):
    (A[i], A[i-1]) = (A[i-1], A[i])
print("№2.1 ", A)

A = [i for i in range(1,6)]

A = A[-1:] + A[:len(A)-1]
print("№2.2 ", A)

A = [1,2,2,3,3,3]

for i in A:
    if A.count(i) == 1:
        print("№2.3 ", i)

A = [1,2,3,3,3,2,2]
maxCount = 1
maxNumber = A[0]
for i in A:
    if A.count(i) > maxCount:
        maxCount = A.count(i)
        maxNumber = i
print("№2.4 ", i)