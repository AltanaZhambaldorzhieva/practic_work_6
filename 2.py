def barmaley(a, b, c, d, e):
    if a >= c and b >= d:
        return True
    if a >= d and b >= c:
        return True
    if a >= c and b >= e:
        return True
    if a >= e and b >= c:
        return True
    if a >= d and b >= e:
        return True
    if a >= e and b >= d:
        return True
    return False


a, b = map(float, input('Введите размер отверстия: ').split(':'))
c, d, e = map(float, input('Введите размер крепости: ').split(':'))
if barmaley(a, b, c, d, e):
    print('Да')
else:
    print('Нет')
