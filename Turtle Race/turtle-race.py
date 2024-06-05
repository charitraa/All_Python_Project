from turtle import *
from random import randint

speed(0)
penup()
goto(-100,200)
for step in range(15):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(160)
    penup()
    backward(170)
    left(90)
    forward(20)

goto(200,250)
write("FinishLine", align='center')
pendown()
right(90)
forward(300)

tur = Turtle()
tur.color('red')
tur.shape('turtle')
tur.penup()
tur.goto(-120,160)
tur.pendown()

tur1 = Turtle()
tur1.color('blue')
tur1.shape('turtle')
tur1.penup()
tur1.goto(-120,130)
tur1.pendown()

tur2 = Turtle()
tur2.color('green')
tur2.shape('turtle')
tur2.penup()
tur2.goto(-120,100)
tur2.pendown()

for turn in range(100):
    speed(0)
    tur.forward(randint(1,5))
    tur1.forward(randint(1,5))
    tur2.forward(randint(1, 5))