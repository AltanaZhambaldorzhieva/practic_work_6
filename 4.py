place = input('Введите координаты: ')

var_1 = ['a', 'c', 'e', 'g']
var_2 = ['b', 'd', 'f', 'h']
num = int(place[-1])
field = place[0]

if field in var_1:
    if num % 2 != 0:
        print('Чёрный')
    else:
        print('Белый')
elif field in var_2:
    if num % 2 != 0:
        print('Белый')
    else:
        print('Чёрный')
