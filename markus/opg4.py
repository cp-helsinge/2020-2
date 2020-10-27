import turtle

def sol(A, B, C):
    turtle.title("SUN")
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    for n in range(1,C):
        turtle.pencolor("red")
        turtle.forward(A)
        turtle.right(B)
    turtle.end_fill()



