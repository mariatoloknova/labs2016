import turtle


def dragon(t, order, size = 1800000, sign = 1):
    if order == 0:
        t.forward(size)
    else:
        t.left(45*sign)
        dragon(t, order-1, size/3, 1)
        t.right(90*sign)
        dragon(t, order-1, size/3, -1)
        t.left(45*sign)


myTurtle = turtle.Turtle()
myTurtle.penup()
myTurtle.setpos(-200, 0)
myTurtle.pendown()
myTurtle.speed(100)
dragon(myTurtle, 12)