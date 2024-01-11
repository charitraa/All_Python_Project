from turtle import speed


love = 'i love u'
speed(0.1)
for i in range(10):
    print(love)
for i in range(10):
    print(i*' ',love)
    for i in range(10):
        print((10-i)*'', love)
for i in [1,2,3]:
    for n in range(len(love)):
        print(love[n:], love[:n])

for i in range(6):
    print(love[:6], (i*2)*' ',
    love[6:])
for i in reversed(range(6)):
    print(love[:6], (i*2)*' ',
    love[6:])