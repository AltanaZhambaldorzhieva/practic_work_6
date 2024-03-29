radius = 6.5
s_circle = 3.14 * (radius ** 2)
a, b = map(float, input('Введите размер ковра: ').split(':'))
s_carpet = a * b
if s_circle >= s_carpet:
    print('Да')
else:
    print('Нет')
