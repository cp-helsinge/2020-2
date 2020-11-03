import turtle
def elefantBalon(lent=100, heig=100, posix=0, posiy=0):
    turtle.penup()
    turtle.goto(float(posix),float(posiy))
    turtle.pendown()
    turtle.forward(lent)
    turtle.right(90)
    turtle.forward(heig)
    turtle.right(90)
    turtle.forward(lent)
    turtle.right(90)
    turtle.forward(heig)
    turtle.right(90)