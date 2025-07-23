def max_number(a,b):
    if a > b:
        return a
    if a < b:
        return b
    else: a==b
    print("Цифры равны")

a = int(input("введите число первое: "))
b = int(input("введите число второе: "))
number = max_number(a,b)
print(number)


def empty_function():
    pass

pass_function = empty_function
print(pass_function)


def even_numbers(n):
    for i in range(0, n, 2):
        yield i

n = int(input("введите число : "))
gen = even_numbers(n)
print(list(gen))

