while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue
    print('Веденная строка достаточной длины')
# Разные другие действия здесь
# continue - продолжать