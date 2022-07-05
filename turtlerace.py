# turtle race using turtle module
from turtle import Turtle,Screen
import random
colors=["red","green","pink","yellow","blue","purple"]
cord=[[-230,-150],[-230,-100],[-230,-50],[-230,0],[-230,50],[-230,100]]
tur=[]
def colandcord(tim,i):
   tim.color(colors[i])
   tim.penup()
   tim.goto(cord[i])
screen=Screen()
screen.setup(height=500,width=500)
bet=screen.textinput(title="Make your bet",prompt="which turtle will win the race?Enter a color(red,green,pink,yellow,blue,purple")
for i in range(6):
    new=Turtle(shape="turtle")
    colandcord(new,i)
    tur.append(new)
if bet:
 israceon=True

while israceon:
    for turtle in tur:
      if turtle.xcor()>230:
         israceon=False
         if turtle.pencolor()==bet:
             print(f"you've won, {turtle.pencolor()} turtle is the winner of the race. ")
         else:
             print(f"you've lost, {turtle.pencolor()} turtle is the winner of the race. ")
      rand_dist=random.randint(0,10)
      turtle.forward(rand_dist)
screen.exitonclick()
