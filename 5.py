var = input('Введите координаты: ')
l1, num1 = var[0], int(var[1])
l2, num2 = var[-2], int(var[-1])

let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
right = (3**2 + 2**2)**0.5

a = let.index(l1)
b = let.index(l2)

if ((abs(a-b)+1)**2 + (abs(num1 - num2) + 1)**2)**0.5 == right:
    print('Верно')
else:
    print('Ошибка')
