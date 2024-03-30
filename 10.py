xr1, yr1, xr2, yr2 = map(int, input().split())
xr3, yr3, xr4, yr4 = map(int, input().split())

import turtle as t

t.penup()
t.goto(xr1, yr1)
t.pendown()
for _ in range(2):
    t.forward(xr2-xr1)
    t.right(90)
    t.forward(yr1-yr2)
    t.right(90)

t.penup()
t.goto(xr3, yr3)
t.pendown()
for _ in range(2):
    t.forward(xr4-xr3)
    t.right(90)
    t.forward(yr3-yr4)
    t.right(90)

if abs(xr1 > xr4 or xr2 < xr3 or yr1 < yr4 or yr2 > yr3):
    print('Прямоугольники лежат вне друг друга, не касаясь')
elif abs(xr1 == xr4 or xr2 == xr3 or yr1 == yr4 or yr2 == yr3):
    print('Прямоугольники имеют касание')
elif abs(xr1 > xr3 and xr2 < xr4 and yr1 < yr3 and yr2 > yr4):
    print('Один лежит внутри другого не касаясь')
elif abs(xr1 > xr4 or xr2 < xr3 or yr1 < yr4 or yr2 > yr3) and not abs(xr1 == xr4 or xr2 == xr3
                                                                or yr1 == yr4 or yr2 == yr3):
    print('Имеют пересечение')
