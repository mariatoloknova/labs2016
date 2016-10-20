dictionary = dict()
N = int(input())
file = open("input2", "r")
for line in file:
    line = line.rstrip().split(":")
    line[0] = line[0][:-1]
    line[1] = line[1][1:]
    line[1] = line[1].split()
    for language in line[1]:
        if language not in dictionary:
            dictionary[language] = [line[0]]
        else:
            dictionary[language].append(line[0])

for i in range(N):
    language = input()
    print(*dictionary[language])

file.close()