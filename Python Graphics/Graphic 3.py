from turtle import *
from random import randint
th = 30
lt(30)
colormode(255)
for i in range(6):
    r = randint(0,255)
    for j in range(5):
        fillcolor(r,255-r,r)
        begin_fill()
        rt(30)
        fd(50)
        if j == 0:
            x,y = position()
            h =heading()
        for k in [th,180-th]*2:
            lt(k)
            fd(50)
        th += 30
        end_fill()
    up()
    goto(x,y)
    down()
    seth(h-30)
    th = 30
done()