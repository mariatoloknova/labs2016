class Shape:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def __str__(self):
        return "Shape with {} in heigth and {} in width".format(self.height, self.width)

class Triangle(Shape):
    def area(self):
        return 0.5*self.height*self.width


class Rectangle(Shape):
    def area(self):
        return self.height*self.width


class Mother:
    def __init__(self, age, name, secret):
        self.age = age
        self.name = name
        self.__secret = secret

    def get_secret(self):
        return self.__secret

    def __str__(self):
        return "I am mother. My name is {}. I am {} years old. I {}".format(self.name, self.age, self.__secret)


class Daughter(Mother):
    def __init__(self, age, eye_color, secret, grade):
        super().__init__(age, eye_color, secret)
        self.grade = grade

    def __str__(self):
        return "I am girl. My name is {}. I am {} years old. I am in {} grade. I {}".format(self.name,
                                                                                            self.age, self.grade, self.get_secret())


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age


class Zebra(Animal):
    def __init__(self, name, age, count_of_lines):
        super().__init__(name, age)
        self.count_of_lines = count_of_lines

    def __str__(self):
        return "Zebra {}. It is {} years old. It has {} lines".format(self.name, self.get_age(), self.count_of_lines)


class Dolphin(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def __str__(self):
        return "Dolphin-{} {}. It is {} years old".format(self.species, self.name, self.get_age())


print("Input the height and the width of triangle:", end=" ")
a, b = list(map(int, input().split()))
triangle = Triangle(a, b)
print("Input the height and the width of rectangle:", end=" ")
a, b = list(map(int, input().split()))
rectangle = Rectangle(a, b)
print("The square of triangle is ", triangle.area())
print("The square of rectangle is ", rectangle.area(), end="\n\n\n")


mother = Mother(45, "Olga", "like cats")
daughter = Daughter(15, "Kate", "like dogs", 10)
print("Mother:")
print(mother)
print("Daughter:")
print(daughter)


zebra = Zebra("Andrey", 4, 400)
dolphin = Dolphin("Igor", 2, "Grampus")
print(zebra)
print(dolphin)
