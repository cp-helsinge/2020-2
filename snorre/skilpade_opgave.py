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
elefantballontyper = ["rød ellefantbalon","blå ellefant balon","gul ellefantbalon","super ellefant balon","ikke ellefant balon","hvid ellefantbalon"]

if "suppe ellefant balon" in elefantballontyper:
    print("jaaaaas")
else:
    print("noooooooooooo")

print (elefantballontyper[4])
print (elefantballontyper)
elefantballontyper[4] = "suppe ellefant balon"
print (elefantballontyper[4])
print (elefantballontyper)

if "suppe ellefant balon" in elefantballontyper:
    print("jaaaaas")
else:
    print("noooooooooooo")

for thing in range(0,5):
    dot = 0
    for dot in range(0,len(elefantballontyper)):
        print(elefantballontyper[dot])


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

turtle.exitonclick()