#creating a hirst painting using turtle module in python
import turtle as t
import random


def col():
 colo = random.choice(listc1)
 return colo


screen = t.Screen()

t.colormode(255)
tim = t.Turtle()
listc1 = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85),
          (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53),
          (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159),
          (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82)]
tim.speed("fastest")
u=-200
y=-200
for x in range(10):
 tim.penup()
 tim.goto(y,u)
 for i in range(10):
   colo = col()
   tim.color(colo, colo)
   tim.begin_fill()
   tim.circle(7)
   tim.end_fill()
   tim.penup()
   tim.forward(50)
 u+=50

screen.exitonclick()
