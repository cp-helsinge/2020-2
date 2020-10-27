import turtle

def square(size=100):
    turtle.speed(6)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.left(24)

for n in range(1,16):
    square(275)


input()
