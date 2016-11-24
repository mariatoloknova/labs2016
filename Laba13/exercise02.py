import turtle


def koch(t, order, size = 500):

    if order == 0:
        t.forward(size)
    else:
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)


myTurtle = turtle.Turtle()
myTurtle.penup()
myTurtle.setpos(-200, 0)
myTurtle.pendown()
koch(myTurtle, 3)