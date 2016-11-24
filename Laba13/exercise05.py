import turtle


def levy(t, order, size = 18000):
    if order == 0:
        t.forward(size)
    else:
        t.left(45)
        levy(t, order-1, size/3)
        t.right(90)
        levy(t, order-1, size/3)
        t.left(45)


myTurtle = turtle.Turtle()
myTurtle.penup()
myTurtle.setpos(-200, 0)
myTurtle.pendown()
levy(myTurtle, 6)