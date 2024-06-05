from turtle import *
import turtle
size = 8
length = 50
startx = -200
starty = -200


def nestedloop():

    turtle.speed(0)

    for row1 in range(size):
        for col1 in range(size):
            if (row1+col1) % 2 == 0:
                turtle.fillcolor("black")
            else:
                turtle.fillcolor("blue")
                turtle.begin_fill()
                a = startx + col1*length
                b = starty + row1*length
                turtle.penup()
                turtle.setpos(a, b)
                turtle.pendown()
                for i in range(4):
                    turtle.forward(length)
                    turtle.left(90)
                    turtle.end_fill()


nestedloop()
turtle.done()
j
je
jes
jesi
jesis
jesish
jesishkhadk

jss
jsa
