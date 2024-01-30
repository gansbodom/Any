integer = int(input('Введите целое число: '))

print('Верно ли, что было подучено трёхзначное число?:')
if len(str(integer)) == 3:
    print('Да')
else:
    print('Нет')
