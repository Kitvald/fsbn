while True:
    a = input("Введите ваш пароль: ")
    password = "qwerty"
    if a == password:
        print("Пароль введен верно")
        break
    else:
        a != password
        print("Пароль введен не верно")
        # следует ли добавить break после введения неправильного пароля