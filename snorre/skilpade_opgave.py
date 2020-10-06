import turtle
turtle.shape("turtle")
turtle.shapesize(10)
turtle.title("hello")
turtle.forward(300)

n = 5
for n in range(1,5):
    turtle.forward(100)
    turtle.right(90)



turtle.home()
o = 0
for o in range(0,255):

    turtle.right(1)
    turtle.forward(100)
    turtle.forward(-100)
    turtle.pensize(o)
    turtle.pencolor((0, 0, o/255))
    turtle.title(str(o))

while 1 == 1:
    turtle.right(0)