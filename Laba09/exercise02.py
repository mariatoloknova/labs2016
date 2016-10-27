#!/usr/bin/python3

# подключаем модуль разбора параметров командной строки
import argparse
# подключаем модуль sys
import sys

# создаём парсер и описываем все параметры командной строки, которые может
# принимать наша программа
parser = argparse.ArgumentParser(
    # краткое описание программы
    description='Калькулятор для самых маленьких'
)

# описываем позиционные параметры
parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'values',
    # название параметров, которое будет отображено в справке
    metavar='VALUES',
    # сообщаем что ожидаются числа с плавающей запятой
    type=float,
    # параметров будет не меньше одного
    nargs=2,
    # краткое описание параметров
    help='входная последовательность чисел'
)

# описываем опцию
parser.add_argument(
    # короткое название опции
    '-a',
    # длинное название опции
    '--action',
    # название параметра, которое будет отображено в справке
    metavar='VALUE',
    # сообщаем парсеру, что ожидается число с плавающей запятой
    type=str,
    # парсер сохранит значение параметра, если встретит эту опцию
    action='store',
    # краткое описание опции
    help='Чё делать с аргументами?'
)

# описываем опцию
parser.add_argument(
    # короткое название опции
    '-v',
    # длинное название опции
    '--verbose',
    # парсер сохранит значение True, если встретит эту опцию
    action='store_true',
    # краткое описание опции
    help='Нормально вывести выражение'
)

# вызываем функцию разбора параметров командной строки
args = parser.parse_args()

# проверяем, что --action передан
if not args.action:
    # выводим сообщение об ошибке в стандартный поток вывода ошибок (stderr)
    print(
        'Необходимо указать параметр --action',
        file=sys.stderr
    )
    # завершаем программу
    sys.exit(-1)

if args.verbose:
    if args.action == "+":
        print(args.values[0], "+", args.values[1], "=", args.values[0] + args.values[1])
    elif args.action == "-":
        print(args.values[0], "-", args.values[1], "=", args.values[0] - args.values[1])
    elif args.action == "/":
        print(args.values[0], "/", args.values[1], "=", args.values[0] / args.values[1])
    elif args.action == "*":
        print(args.values[0], "*", args.values[1], "=", args.values[0] * args.values[1])
else:
    if args.action == "+":
        print(args.values[0] + args.values[1])
    elif args.action == "-":
        print(args.values[0] - args.values[1])
    elif args.action == "/":
        print(args.values[0] / args.values[1])
    elif args.action == "*":
        print(args.values[0] * args.values[1])
