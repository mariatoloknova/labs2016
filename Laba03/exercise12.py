import turtle

turtle.shape("turtle")

def duga():
    for i in range(180):
        turtle.forward(1)
        turtle.right(1)

def fulduga():
    duga()
    for i in range(180):
        turtle.forward(0.1)
        turtle.right(1)

turtle.left(90)
for i in range(2):
    fulduga()