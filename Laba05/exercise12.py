with open("input", "r") as file:
    n = file.readline()
    houses = file.readlines()
    file.close()
houses = [i.rstrip() for i in houses]
houses = list(map(int, houses))
finish = 0
MAX_SQUARE = 0
while(0 in houses[finish:]):
    start = finish
    finish = houses.index(0)
    MIN_HEIGHT = min(houses[start:finish])
    if MIN_HEIGHT*len(houses[start:finish]) > MAX_SQUARE:
        MAX_SQUARE = len(houses[start:finish]) * MIN_HEIGHT
    finish += 1
MIN_HEIGHT = min(houses[finish:])
if MIN_HEIGHT*len(houses[finish:]) > MAX_SQUARE:
    MAX_SQUARE = len(houses[finish:]) * MIN_HEIGHT

with open("output.txt", "w") as file:
    file.write(str(MAX_SQUARE) + "\n" + str(MIN_HEIGHT))