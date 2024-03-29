n = int(input('Введите количество суши: '))

if n % 5 == 0 or n % 7 == 0 or ((n - 5) % 7 == 0) or ((n - 7) % 5 == 0) or n % 12 == 0:
    print('да')
else:
    print('нет')
