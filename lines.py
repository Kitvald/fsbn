def max_number(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else: a==b
    print("Цифры равны")

a = int(input("введите число первое: "))
b = int(input("введите число второе: "))
number = max_number(a,b)
print(number)


def empty_function():
    pass

print(empty_function)


def even_numbers(n):
    for i in range(2, n, 2):
        yield i

gen = even_numbers(88)
print(list(gen))

