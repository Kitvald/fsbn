try:
    print("Доступные операции:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Умножение")
    print("4 - Деление")

    operation = input("Выберите операцию (1/2/3/4): ")

    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))

    if operation == '1':
        result = num1 + num2
        print(f"Результат сложения: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"Результат вычитания: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"Результат умножения: {result}")
    elif operation == '4':
        result = num1 / num2
        print(f"Результат деления: {result}")
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
