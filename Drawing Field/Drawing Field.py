from turtle import *
from turtle import Turtle, Screen

def drag(i, j):
    tur.ondrag(None)
    tur.setheading(tur.towards(i, j))
    tur.goto(i, j)
    tur.ondrag(drag)

ws = Screen()

tur = Turtle('turtle')
tur.speed('fastest')
tur.color('red')
tur.ondrag(drag)

ws.mainloop()