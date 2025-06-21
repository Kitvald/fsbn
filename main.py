try:
    num1 = int(input("Введите первое число для сложения: "))
    num2 = int(input("Введите второе число для сложения: "))
    result = num1 + num2
    print(f"Результат: {result}")

    num1 = int(input("Введите первое число для вычитания: "))
    num2 = int(input("Введите второе число для вычитания: "))
    result = num1 - num2
    print(f"Результат: {result}")

    num1 = int(input("Введите первое число для умножения: "))
    num2 = int(input("Введите второе число для умножения: "))
    result = num1 * num2
    print(f"Результат: {result}")

    num1 = float(input("Введите первое число для деления: "))
    num2 = float(input("Введите второе число для деления: "))
    result = num1 / num2
except ValueError:
    print("Ошибка: введено не число!")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
    print(f"Результат: {result}")