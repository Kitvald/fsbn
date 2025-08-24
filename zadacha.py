def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i


def empty_function():
    pass




def test_max_number():
    assert max_number(3, 2) == 3, "Ошибка: max_number(3, 2) должна быть равна 3"
    assert max_number(-1, 1) == 1, "Ошибка: max_number(-1, 1) должна быть равна 1"
    assert max_number(0, 0) == 0, "Ошибка: max_number(0, 0) должна быть равна 0"

test_max_number()
print("Все тесты пройдены!")

a = int(input("введите число первое: "))
b = int(input("введите число второе: "))
number = max_number(a, b)
print(number)

pass_function = empty_function()
print(pass_function)

n = int(input("введите число : "))
gen = even_numbers(n)
print(list(gen))
