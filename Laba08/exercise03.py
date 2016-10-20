import string

file = open("../LICENSE", "r")
A = {}
exclude = set(string.punctuation)
line = file.readline().rstrip()
while line:
    line = line.rstrip()
    for element in exclude:
        while element in line:
            line = line.replace(element, " ")
    for word in line.split():
        if word not in A:
            A[word.lower()] = 1
        else:
            A[word.lower()] += 1
    line = file.readline()
print(sorted(A.items(), key = lambda x: x[1], reverse = True)[0][0])