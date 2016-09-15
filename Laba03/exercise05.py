import turtle

turtle.shape('turtle')

for j in range(1,31):
    turtle.pendown()
    for i in range(4):
        turtle.forward(10*j)
        turtle.left(90)
    turtle.penup()
    turtle.goto(-5*j, -5*j)
