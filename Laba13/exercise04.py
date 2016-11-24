import turtle


def misterMink(t, order, size = 200):

    if order == 0:
        t.forward(size)
    else:
        misterMink(t, order-1, size/3)
        t.left(90)
        misterMink(t, order-1, size/3)
        t.right(90)
        misterMink(t, order-1, size/3)
        t.right(90)
        misterMink(t, order-1, size/3)
        misterMink(t, order-1, size/3)
        t.left(90)
        misterMink(t, order - 1, size / 3)
        t.left(90)
        misterMink(t, order - 1, size / 3)
        t.right(90)
        misterMink(t, order - 1, size / 3)

myTurtle = turtle.Turtle()
myTurtle.penup()
myTurtle.setpos(-200, 0)
myTurtle.pendown()
misterMink(myTurtle, 2)