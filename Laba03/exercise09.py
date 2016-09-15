import turtle
import time
import math

turtle.shape("turtle")

#time.sleep(1)

def poly(n, a):
    for i in range(n):
        turtle.forward(a)
        turtle.left(360/n)
        #time.sleep(1)

turtle.left(90)

for i in range(3, 11):
    R = i*15
    a = 2*R*math.sin(math.pi/i)
    turtle.left(360/(2*i))
    poly(i, a)
    turtle.right(360/(2*i)+90)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.left(90)