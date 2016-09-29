arr = list(map(int, input().split()))
newArr = []

for i in range(len(arr)-1):
    if arr[i+1] != 2 and arr[i] == 2:
        continue
    else:
        newArr.append(arr[i])
newArr.append(arr[-1])
print(int( sum(newArr) / len(newArr) ))