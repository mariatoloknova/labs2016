dictionary = dict()
file = open("en-ru2", "r")
for line in file:
    line = line.rstrip().split("\t-\t")
    dictionary[line[1]] = line[0]
file.close()

file = open("ru-en", "a")
for element in sorted(dictionary.items()):
    file.write(element[0] + "\t-\t" + element[1] + "\n")
file.close()