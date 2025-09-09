password = 'qwerty'

while True:
    a = input('Введите пароль:  ')
    if a == password:
        print("Пароль верный")
        break
    else:
        print("Пароль не верный")