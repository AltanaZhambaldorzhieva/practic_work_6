xc1, yc1, r1 = map(int, input().split())
xc2, yc2, r2 = map(int, input().split())

import turtle as t

t.penup()
t.goto(xc1, yc1)
t.pendown()
t.circle(r1)

t.penup()
t.goto(xc2, yc2)
t.pendown()
t.circle(r2)


if (abs(yc2-yc1)**2 + abs(xc2-xc1)**2)**0.5 > r1+r2:
    print('Окружности лежат одна вне другой, не касаясь')
elif (abs(yc2-yc1)**2 + abs(xc2-xc1)**2)**0.5 == r1+r2:
    print('Окружности имеют внешнее касание')
elif (abs(yc2-yc1)**2 + abs(xc2-xc1)**2)**0.5 == abs(r1-r2):
    print('Окружности имеют внутреее касание')
else:
    print('Одна окружность лежит внутри другой, не касаясь')
