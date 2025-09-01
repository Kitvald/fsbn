a = input("Введите ваш пароль: ")
password = "qwerty"

while a != password:
    if a != password:
        a = input("Введите ваш пароль: ")
else:
    print("вы ввели тот самый пароль, перепарольте")
    a = input("Введите ваш пароль: ")
