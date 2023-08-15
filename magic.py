from turtle import *
import turtle as tur
import random
import math

tur.setup(900,500)
tur.title("magic graphic")
a1=tur.Turtle()
b1=tur.Turtle()
c1=tur.Turtle()
d1=tur.Turtle()
e1=tur.Turtle()
f1=tur.Turtle()
g1=tur.Turtle()

a1.color('green')
b1.color('purple')
c1.color('red')
d1.color('yellow')
e1.color('black')
f1.color('orange')
g1.color('blue')

turtlist = []
turtlist.append(a1)
turtlist.append(b1)
turtlist.append(c1)
turtlist.append(d1)
turtlist.append(e1)
turtlist.append(f1)
turtlist.append(g1)

tur.speed(1)
tur.tracer(0)
tur.hideturtle()
sum = 0
count = 0
for j in range(100):
    for i in range(10000):
        for turt in turtlist:
            turt.seth(random.randrange(0,360,90))
            turt.fd(10)
        tur.update()
    for turt in turtlist:
       sum += math.sqrt(turt.xcor()*turt.xcor() + turt.ycor()*turt.ycor()/10*2*math.sqrt(turt.xcor()*turt.xcor()+ turt.ycor()*turt.ycor())/100)
       count +=1
    for turt in turtlist:
        turt.clear()
        turt.up
        turt.goto(0,0)
        turt.down()
        print(sum/count)