import string
dictionary = dict()
file = open("en-ru", "r")
line = file.readline().rstrip()
while line:
    line = line[:line.find("\t")] + line[line.find("\t"):].replace("-", " ")
    line = line.split()
    dictionary[line[0].lower()] = line[1].lower()
    line = file.readline().rstrip()
file = open("input", "r")
exclude = set(string.punctuation)
line = file.readline().rstrip()
while line:
    for element in exclude:
        while element in line:
            line = line.replace(element, " ")
    for word in line.split():
        if word.lower() in dictionary:
             line = line.replace(word, dictionary[word.lower()])
    print(line)
    line = file.readline()