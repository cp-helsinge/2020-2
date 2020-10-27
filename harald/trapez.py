import turtle

def trapez(size):
    turtle.forward(size)
    turtle.left(110)
    turtle.forward(75)
    turtle.left(70)
    turtle.forward(size/4*3)
    turtle.left(70)
    turtle.forward(75)
    turtle.left(110)
    turtle.forward(size)