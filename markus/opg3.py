import turtle
turtle.speed(0)
turtle.hideturtle()
def sol(A, B, Y, X):
    turtle.title("SUN")
    turtle.shape("turtle")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for n in range(1,50):
        turtle.pencolor("red")
        turtle.forward(A)
        turtle.right(B)
    turtle.end_fill()

A = int(input("Size. Normal size is 50 = "))
B = int(input("Angle. Normal angle is 75 = "))
sol(A, B)
# Main er sol(50, 75)

input("Done. Press enter when your done looking")