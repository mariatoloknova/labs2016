import turtle

def koch(t, order, size = 600):

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


def snowflake(t, order, size = 400):
    for i in range(6):
        koch(t, order, size)
        t.right(120)


myTurtle = turtle.Turtle()
myTurtle.penup()
myTurtle.setpos(-200, 0)
myTurtle.pendown()
snowflake(myTurtle, 2)