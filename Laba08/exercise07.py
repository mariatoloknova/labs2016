import re

dictionaryRU = dict()
dictionaryEN = dict()

# Выкачиваем русско-английский словарь
with open("ru-en8", "r") as file:
    for line in file:
        line = line.rstrip().split("\t-\t")
        dictionaryRU[line[0]] = re.sub(r'[=,\s]', " ", line[1]).split()

# Выкачиваем англо-русский словарь
with open("en-ru8", "r") as file:
    for line in file:
        line = line.rstrip().split("\t-\t")
        dictionaryEN[line[0]] = re.sub(r'[,=\s]', " ", line[1]).split()

# Синхронизируем англо-русский словарь с русско-английским
for wordRU in dictionaryRU:
    for wordEN in dictionaryRU[wordRU]:
        if wordEN in dictionaryEN:
            if wordRU not in dictionaryEN[wordEN]:
                try:
                    dictionaryEN[wordEN].append(wordRU)
                except AttributeError:
                    dictionaryEN[wordEN] = [dictionaryEN[wordEN]]
                    dictionaryEN[wordEN].append(wordRU)
        else:
            dictionaryEN[wordEN] = wordRU

# Сихронизируем русско-английский словарь с англо-русским
for wordEN in dictionaryEN:
    for wordRU in dictionaryEN[wordEN]:
        if wordRU in dictionaryRU:
            if wordEN not in dictionaryRU[wordRU]:
                try:
                    dictionaryRU[wordRU].append(wordEN)
                except AttributeError:
                    dictionaryRU[wordRU] = [dictionaryRU[wordRU]]
                    dictionaryRU[wordRU].append(wordEN)
        else:
            dictionaryRU[wordRU] = wordEN

# Перезапись англо-русского словаря
with open("new_en-ru8", "w") as file:
    for wordEN in dictionaryEN:
        if type(dictionaryEN[wordEN]) == str :
            file.write(wordEN + "\t-\t" + dictionaryEN[wordEN] + "\n")
        else:
            file.write(wordEN + "\t-\t" + ", ".join(dictionaryEN[wordEN]) + "\n")

# Перезапись русско-английского словаря
with open("new_ru-en8", "w") as file:
    for wordRU in dictionaryRU:
        if type(dictionaryRU[wordRU]) == str :
            file.write(wordRU + "\t-\t" + dictionaryRU[wordRU] + "\n")
        else:
            file.write(wordRU + "\t-\t" + ", ".join(dictionaryRU[wordRU]) + "\n")