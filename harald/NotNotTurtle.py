import turtle
size = 39
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

#size*0.73
#size = input("hvor stor skal den være? ")
trapez(55)

input()     