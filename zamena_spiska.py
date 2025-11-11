from itertools import zip_longest

list = [1, 2, 3, 4, 'cat']
list[4], list[0] = list[0], list[4]
print(list)



# ДЗ: задание сложение элементов списков
data = [1, 2, 5, 4]
data1 = [2, 4, 5]
result = [data + data1 for data, data1 in zip_longest(data, data1, fillvalue=0)]
print(result)
#я не уверен в том что задействование библиотек верно, может есть другой вариант, но я не понял