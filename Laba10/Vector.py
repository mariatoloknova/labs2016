import math


class Vector:
    def __init__(self, string):
        self.x, self.y = string.split(",")
        self.x = float(self.x)
        self.y = float(self.y)

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __add__(self, other):
        string = str(self.x + other.x) + "," + str(self.y + other.y)
        return Vector(string)

    def __iadd__(self, other):
        string = str(self.x + other.x) + "," + str(self.y + other.y)
        return Vector(string)

    def __sub__(self, other):
        string = str(self.x - other.x) + "," + str(self.y - other.y)
        return Vector(string)

    def __isub__(self, other):
        string = str(self.x - other.x) + "," + str(self.y - other.y)
        return Vector(string)

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y

    def __truediv__(self, a):
        string = str(self.x / a) + "," + str(self.y / a)
        return Vector(string)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)


# inputting the vectors
vectors = []
print("How many vectors do we have?")
N = int(input())
print("\nInput these vectors in format 'x,y':")
for i in range(N):
    vectors.append(Vector(input()))

# finding the farthest points
max_points = [Vector("0,0")]
for vector in vectors:
    if vector.length() > max_points[0].length():
        max_points = [vector]
    elif vector.length() == max_points[0].length():
        max_points.append(vector)

# print the farthest points
print("\nThe farthest points:", end = " ")
for vector in max_points:
    print(vector)

# Find the center of mass
print("The center of mass:", end = " ")
numerator = Vector("0,0")
denominator = len(vectors)
for vector in vectors:
    numerator += vector
print(numerator/denominator)

# Find the biggest perimeter
print("The biggest perimeter:", end = " ")
sides = []
for i in range(len(vectors)):
    sides.append([])
    for j in range(i+1, len(vectors)):
        sides[i].append((vectors[i]-vectors[j]).length())
max_length = []
sides.pop()
max_point = 0
for n in range(3):
    for i in range(len(sides)):
        if max(sides[i]) > max_point:
            max_point = max(sides[i])
            m = i
    max_length.append(sides[m].pop(sides[m].index(max_point)))
    if not sides[m]:
        sides.pop(m)
    max_point = 0
print(sum(max_length))

# Find new vectors to find squares
new_vectors = []
for i in range(len(vectors)):
    for j in range(i+1, len(vectors)):
        new_vectors.append(vectors[j]-vectors[i])

# Find the biggest square
print("The biggest square:", end = " ")
squares = []
for i in range(len(new_vectors)):
    squares.append([])
    for j in range(i+1, len(new_vectors)):
        new_a = new_vectors[j] / (new_vectors[j]*new_vectors[j])/(new_vectors[i]*new_vectors[j])
        h = new_vectors[i] - new_a
        squares[i].append(0.5*h.length()*new_vectors[j].length())
max_square = []
squares.pop()
max_point = 0
for i in range(len(squares)):
    if max(squares[i]) > max_point:
        max_point = max(squares[i])
        m = i
print(squares[m].pop(squares[m].index(max_point)))