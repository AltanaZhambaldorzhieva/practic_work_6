n, m = map(float, input('Введите размер квартала: ').split(':'))
k = int(input('На сколько делим: '))

if (((n*m)-n) == k) or (((n*m)-m) == k):
    print('Успешно')
else:
    print('Не осуществимо')
