string = input()
a = string.find('h') + 1
b = string.rfind('h')
string = string[:a] + string[a:b].replace('h', 'H') + string[b:]
print(string)