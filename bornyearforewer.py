
bornyear = int(input('Ввведите год рождения А.С.Пушкина: '))
while bornyear != 1799:
    bornyear = int(input('Ввведите год рождения А.С.Пушкина: '))
if bornyear == 1799:
    bornday = str(input('Введите день рождения А.С.Пушкина: '))
    while bornday != '6 июня':
        bornday = str(input('Введите день рождения А.С.Пушкина: '))
if bornday == '6 июня':
    print('Верно')