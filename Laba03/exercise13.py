import turtle

turtle.shape("turtle")

def circle(R):
    for i in range(360):
        turtle.forward(R)
        turtle.left(1)

turtle.goto(0, 0)
turtle.left(90)
turtle.begin_fill()
turtle.color('yellow')
circle(1)
turtle.end_fill()
turtle.color('black')
turtle.penup()

turtle.goto(-75, 20)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
circle(0.1)
turtle.end_fill()
turtle.penup()

turtle.goto(-25, 20)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
circle(0.1)
turtle.end_fill()
turtle.penup()

turtle.left(180)
turtle.goto(-55, 10)
turtle.pendown()
turtle.color('black')
turtle.width(6)
turtle.forward(20)
turtle.penup()

turtle.goto(-25 ,-10)
turtle.pendown()
turtle.color('red')
turtle.width(8)
for i in range(180):
    turtle.forward(0.5)
    turtle.right(1)

input()