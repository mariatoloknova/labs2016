import turtle

turtle.shape("turtle")

def circle(n):
    for i in range(360):
        turtle.forward(n/2)
        turtle.left(1)
    for i in range(360):
        turtle.forward(n/2)
        turtle.right(1)

for i in range(1,11):
    circle(i)