from turtle import*
bgcolor('black')
speed(50)
n=0
colormode(255)
while n < 200:
    right(n)
    forward(n * 3)
    color(n,255-n,n%30*8)
    n+=1