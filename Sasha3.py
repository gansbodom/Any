a = float(input('Введите число a: '))
b = float(input('Введите число b: '))
x = float(input('Введите число x: '))

#Вложенные условные операторы
if x >= a:
    if x <= b:
        print(f'Число {x} принадлежит отрезку [{a}, {b}]')
    else:
        print(f'Число {x} не принадлежит отрезку [{a}, {b}]')
else:
    print(f'Число {x} не принадлежит отрезку [{a}, {b}]')
    
#Сложные условия
if a <= x <= b:
    print(f'Число {x} принадлежит отрезку [{a}, {b}]')
else:
    print(f'Число {x} не принадлежит отрезку [{a}, {b}]')