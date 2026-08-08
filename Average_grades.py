students = [
    {"name": "Frodo", "grades": [87, 48, 98]}, # 77.66
    {"name": "Cem", "grades": [93, 64, 45]}, # 67,33
    {"name": "Pipin", "grades": [70, 65, 90]}, #75
] #73.33 общий ср балл


def calculate_average(grades):
    return sum(grades) / len(grades)

avg_stud = []

for student in students:
    average = calculate_average(student["grades"])
    avg_stud.append(average)
    if average >= 75:
        print(f"Cтудент {student["name"]}\nСредний балл: {average}\nСтатус: Успешен\n")
    else:
        print(f"Cтудент {student["name"]}\nСредний балл: {average}\nСтатус: Не успешен\n")


total_avg = calculate_average(avg_stud)
print("Общий средний балл", total_avg)

min_average = avg_stud.index(min(avg_stud))
asdqwe = students.pop(min_average)
students.append({"name": "Gendalf", "grades": [99, 100, 98]})
#print(students)


for student in students:
    average = calculate_average(student["grades"])
    if average >= 75:
        print(f"Cтудент {student["name"]}\nСредний балл: {average}\nСтатус: Успешен\n")
    else:
        print(f"Cтудент {student["name"]}\nСредний балл: {average}\nСтатус: Не успешен\n")











