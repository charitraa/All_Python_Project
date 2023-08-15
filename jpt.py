from turtle import *
import turtle
import random
speed(100)


def drawRandom():
    a = random.randrange(-150, 150)
    b = random.randrange(-150, 150)
    leng = random.randrange(75)
    shape = random.randrange(1, 4)

    moveturtle(a, b)

    if shape == 1:
        drawSquare(leng)
    elif shape == 2:
        drawTriangle(leng)
    elif shape == 3:
        leng = leng % 4
        drawCircle(leng)


def drawshape(side, leng):
    ang = 360.0 / side
    for side in range(side):
        turtle.forward(leng)
        turtle.right(ang)


def moveturtle(a, b):
    turtle.penup()
    turtle.goto(a, b)
    turtle.pendown()


def drawSquare(leng):
    drawshape(4, leng)


def drawTriangle(leng):
    drawshape(3, leng)


def drawCircle(leng):
    drawshape(360, leng)


for shape in range(100):
    drawRandom()

turtle.done()

