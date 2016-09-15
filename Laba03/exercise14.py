import turtle

turtle.shape("turtle")

def star(n):
    for i in range(n):
        turtle.forward(200)
        turtle.right(180)
        turtle.right(360/(2*n))

star(5)
