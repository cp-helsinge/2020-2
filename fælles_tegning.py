# Use modules
# from mod1 import * # her importerer vi funktioner fra filen mod1.py
from simon.turtle_func import * # her importerer vi funktioner fra filen mod2.py
#from harald.turtle_func import *
#from alvin.turtle_func import *
#from jesper.turtle_func import *
#from henrik.turtle_func import *
#from markus.turtle_func import *
#from matias.turtle_func import *
#from snorre.turtle_func import *

import turtle # her importerer vi hele turtle modulet

turtle.speed("fastest")
turtle.color(0.4,0,1)
turtle.pensize(4)

def move(x=0,y=0):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()


# Test her
tester()

"""
def flower():
  for n in range(1,11):
    circle(50)
    turtle.left(36)

def weird_flower():
  for n in range(1,10):
    square(100)
    triangle(200)
    circle(50)
    turtle.left(36)

for n in range(-4,5):
  move(n*200,-300)
  flower()

for n in range(-2,3):
  move(n*350,200)
  weird_flower()

square()
"""

input()

# Test 3 og 4
# og 5 og seks
