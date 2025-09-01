try:
    number = abs(int(input("Введите ваше число: ")))
except ValueError:
    print("Ошибка! Введите целое число, а не текст.")
while number > -1:
    print("Счетчик =", number)
    number -= 1
    