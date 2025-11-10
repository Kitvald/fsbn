

data =  [i for i in range(0, 101) if i % 2 == 0]
print(sum(data))


data1 =  [i * i for i in range(0, 10) if i % 2 == 1]
print(data1)


def numbers():
    counts = 0
    while True:
        current_number = int(input("Введите число: "))
        if current_number <= 0:
            break
        counts += 1
    return counts
print(numbers())