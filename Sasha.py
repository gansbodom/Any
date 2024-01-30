month = int(input('Введите номер месяца: '))

if 1 <= month <= 2 or month == 12:
    print('Время годя - зима')
    if month == 1:
        print('Январь')
    elif month == 2:
        print('Февраль')
    elif month == 12:
        print('Декабрь')
if 3 <= month <= 5:
    print('Время года - весна')
    if month == 3:
        print('Март')
    elif month == 4:
        print('Апрель')
    elif month == 5:
        print('Май')
if 6 <= month <= 8:
    print('Время года - лето')
    if month == 6:
        print('Июнь')
    elif month == 7:
        print('Июль')
    elif month == 8:
        print('Август')
if 9 <= month <= 11:
    print('Время года - осень')
    if month == 9:
        print('Сентябрь')
    elif month == 10:
        print('Октябрь')
    elif month == 11:
        print('Ноябрь')
else:
    print('Ошибка')
