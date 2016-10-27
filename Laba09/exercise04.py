#!/usr/bin/python3

# подключаем модуль разбора параметров командной строки
import argparse
# подключаем модуль sys
import sys
import os

def makeDir(path, files):
    dirPath = []
    for file in files:
        dirPath.append()
    return dirPath

def tree(dir, padding, all, include, exclude, print_files):
    print(padding[:-1] + '+-' + os.path.basename(os.path.abspath(dir)) + '/')
    padding = padding + ' '
    files = []
    if print_files:
        files = os.listdir(dir)
    else:
        files = [x for x in os.listdir(dir) if os.path.isdir(dir + os.sep + x)]
    count = 0
    for file in files:
        count += 1
        print(padding + '|')
        path = dir + os.sep + file
        if os.path.isdir(path):
            if count == len(files):
                tree(path, padding + ' ', all, include, exclude, print_files)
            else:
                tree(path, padding + '|', all, include, exclude, print_files)
        else:
            print(padding + '+-' + file)

# создаём парсер и описываем все параметры командной строки, которые может
# принимать наша программа
parser = argparse.ArgumentParser(
    # краткое описание программы
    description='Выведение файлов'
)

# описываем позиционные параметры
parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'values',
    # название параметров, которое будет отображено в справке
    metavar='VALUES',
    # сообщаем что ожидаются числа с плавающей запятой
    type=str,
    # параметров будет не меньше одного
    nargs="+",
    # краткое описание параметров
    help='входная последовательность файлов'
)

# описываем опцию
parser.add_argument(
    # длинное название опции
    '--include',
    # название параметра, которое будет отображено в справке
    metavar='VALUE',
    # сообщаем парсеру, что ожидается число с плавающей запятой
    type=str,
    # парсер сохранит значение параметра, если встретит эту опцию
    action='store',
    # краткое описание опции
    help='Чё отображаем?'
)

# описываем опцию
parser.add_argument(
    # длинное название опции
    '--exclude',
    # название параметра, которое будет отображено в справке
    metavar='VALUE',
    # сообщаем парсеру, что ожидается число с плавающей запятой
    type=str,
    # парсер сохранит значение параметра, если встретит эту опцию
    action='store',
    # краткое описание опции
    help='Чё НЕ отображаем?'
)

# описываем опцию
parser.add_argument(
    # длинное название опции
    '--foldersonly',
    # парсер сохранит значение True, если встретит эту опцию
    action='store_true',
    # краткое описание опции
    help='Не отображаем файлы'
)

# описываем опцию
parser.add_argument(
    # длинное название опции
    '--all',
    # парсер сохранит значение True, если встретит эту опцию
    action='store_true',
    # краткое описание опции
    help='Отображать скрытые файлы и директории'
)

# описываем опцию
parser.add_argument(
    # длинное название опции
    '--fullname',
    # парсер сохранит значение True, если встретит эту опцию
    action='store_true',
    # краткое описание опции
    help='Выводим полный текущий путь'
)


# вызываем функцию разбора параметров командной строки
args = parser.parse_args()

# проверяем, что --action передан
if not args.values:
    # выводим сообщение об ошибке в стандартный поток вывода ошибок (stderr)
    print(
        'Укажите хотя бы 1 файл',
        file=sys.stderr
    )
    # завершаем программу
    sys.exit(-1)

homeDir = "/home/les"
currentDir = os.getcwd()
dirPath = []
path = args.values[0]
if path[:2] == "./":
    dirPath.append(currentDir + "/" + path[2:])
elif path[:3] == "../":
    dirPath.append(os.path.dirname(currentDir) + "/" + path[3:])
elif path[:2] == "~/":
    dirPath.append(homeDir + "/" + path[2:])
elif path[:1] == "/":
    dirPath.append(path)
else:
    dirPath.append(currentDir + "/" + path)
dirPath = dirPath[0]
if args.fullname:
    print(dirPath)
all = False
include = None
exclude = None
foldersonly = True
if args.foldersonly:
    foldersonly = False
if args.all:
    all = True
if args.include:
    include = args.include
if args.exclude:
    exclude = args.exclude
tree(dirPath, " ", all, include, exclude, foldersonly)