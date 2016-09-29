rows = int(input())
for rowNum in range (rows+1):
    newValue = 1
    res = [newValue]
    for i in range (rowNum):
        newValue *= ( rowNum - i ) / ( i + 1 )
        res.append(int(newValue))
    print(*res)