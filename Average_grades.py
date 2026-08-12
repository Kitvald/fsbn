def calculate_average(grades):
    for student in grades:
        average = sum(student["grades"]) / len(student["grades"])
        student["average"] = average
    return


def main(average):
    worst_student = min(students, key=lambda students: students["average"])
    students.pop(students.index(worst_student))
    students.append({"name": "Gendalf", "grades": [99, 100, 98]})
    return calculate_average(students)



students = [
    {"name": "Frodo", "grades": [87, 48, 98]}, # 77.66
    {"name": "Cem", "grades": [93, 64, 45]}, # 67,33
    {"name": "Pipin", "grades": [70, 65, 90]}, #75
] #73.33 общий ср балл
calculate_average(students)
main(students)
print(students)
#main(students, avg_stud)
#new_avg_stud = calculate_average(students)
#print("новые баллы", new_avg_stud)











#min_average = avg_stud.index(min(avg_stud))
#asdqwe = students.pop(min_average)
#students.append({"name": "Gendalf", "grades": [99, 100, 98]})


#for student in students:
#    average = calculate_average(student["grades"])
 #   avg_stud.append(average)
 #   if average >= 75:
 #       print(f"Cтудент {student["name"]}\nСредний балл: {average}\nСтатус: Успешен\n")
 #   else:
#        print(f"Cтудент {student["name"]}\nСредний балл: {average}\nСтатус: Не успешен\n")


#total_avg = calculate_average(avg_stud)
#print("Общий средний балл", total_avg)

#min_average = avg_stud.index(min(avg_stud))
#asdqwe = students.pop(min_average)
#students.append({"name": "Gendalf", "grades": [99, 100, 98]})
#print(students)












