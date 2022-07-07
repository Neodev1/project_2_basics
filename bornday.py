bornyear = int(input('Ввведите год рождения А.С.Пушкина: '))
if bornyear == 1799:
    bornday=str(input('Введите день рождения А.С.Пушкина: '))
    if bornday == '6 июня':
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения')