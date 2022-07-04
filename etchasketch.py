#etch a sketch basic app using turtle module
#w for forwards,s for backwards,a for moving left,d for moving right(by 10 degrees)

from turtle import Turtle,Screen
tim = Turtle()
screen=Screen()

def moveforwards():
    tim.forward(10)
def movebackwards():
    tim.backward(10)

def moveright():
  tim.right(10)
def moveleft():
    tim.left(10)
def cleart():
    tim.reset()

screen.listen()
screen.onkey(key="w",fun=moveforwards)
screen.onkey(movebackwards,"s")
screen.onkey(moveleft,"a")
screen.onkey(moveright,"d")
screen.onkey(cleart,"c")









screen.exitonclick()
