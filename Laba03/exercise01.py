n = int(input())
for i in range(1, n):
    if (i % 2 == 0):
        print(i, "even", sep = " ")
    else:
        print(i, "odd", sep = " ")