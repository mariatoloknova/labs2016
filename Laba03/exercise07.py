import turtle

turtle.shape('turtle')
turtle.left(90)

j = 1/(360)
for i in range(1,1800):
    turtle.forward(j*i)
    turtle.left(1)