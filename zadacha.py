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


a = int(input("введите число первое: "))
b = int(input("введите число второе: "))
number = max_number(a, b)
print(number)

pass_function = empty_function()
print(pass_function)

n = int(input("введите число : "))
gen = even_numbers(n)
print(list(gen))

