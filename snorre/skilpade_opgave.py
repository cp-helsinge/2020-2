import turtle
import random
turtle.shape("turtle")
turtle.shapesize(0.1)
turtle.title("hello")
turtle.speed(0)
turtle.forward(300)
turtle.circle(100)
turtle.bgcolor("black")
turtle.pencolor(1, 1, 1)
o = 0
for o in range(0,101):
    turtle.circle(100-o)

n = 5
for n in range(1,5):
    turtle.forward(100)
    turtle.right(90)



turtle.home()
o = 0
for o in range(0,361):

    turtle.right(1)
    turtle.forward(200)
    turtle.forward(-200)
    turtle.pensize(1)
    turtle.pencolor((1, o/360,1 ))
    turtle.title(str(o))

while 1 == 1:
    turtle.right(1)