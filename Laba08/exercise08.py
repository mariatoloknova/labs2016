# ЛУЧШЕ ДЕЛАТЬ ЧЕРЕЗ ОБХОД В ГЛУБИНУ

data = []

with open("input8", "r") as file:
    for line in file:
        data.append(line.rstrip())

N, M, K = list(map(int, data.pop(0).split()))
checked_rooms = set()
rooms = dict()

#####
# Работаю из предположения, что M - реальный номер квартиры. Значит, сначала идём в data[M+K]
# Так же предполагаю, что mi - зашифрованный, а пробегаю по реальным m = mi - ki
#####

checked_rooms.add(M+K)
current_room = M + K
query = [] # Создаём очередь из непосещенных квартир
while N not in rooms and len(checked_rooms) != len(data):
    keys_in_current_room = data[current_room].split(",")
    for key in keys_in_current_room:
        rooms[list(map(int, key.split()))[0]-list(map(int, key.split()))[1]] = list(map(int, key.split()))[1]
    for room in rooms:
        if room not in checked_rooms and room not in query and room < len(data):
            query.append(room)
    current_room = query.pop(0)
    checked_rooms.add(current_room)
print(rooms)