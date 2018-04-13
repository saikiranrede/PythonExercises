my_student = [{"name": "Jose", "school": "Computing", "grades": (66, 77, 88)},
{"name": "John", "school": "Engineering", "grades": (45, 56, 93)}]

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total = total + sum(student["grades"])
        count = count + len(student["grades"])

    return total / count

print(average_grade_all_students(my_student))
