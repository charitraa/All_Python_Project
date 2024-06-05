from turtle import *
import turtle

tur = turtle.Turtle()

tur.speed(100)

tur.getscreen().bgcolor("black")
tur.color("white")

tur.pendown()

def triangle(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):

            turtle.forward(size)
            triangle(turtle, size/3)

            turtle.left(216)

triangle(tur, 360)
turtle.done()