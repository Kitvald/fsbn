def adding_lists():
    result = []
    for i in range(max(len(data), len(data1))):
        a = data[i] if i < len(data) else 0
        b = data1[i] if i < len(data1) else 0
        result.append(a + b)
    return result


data = [1, 2, 5, 6, 5, 5, 5]
data1 = [2, 4, 5]
print(adding_lists())