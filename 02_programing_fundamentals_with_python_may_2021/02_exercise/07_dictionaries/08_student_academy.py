n = int(input())

students_dict = {}

for _ in range(0, n):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_dict:
        students_dict[student_name] = [student_grade]
    else:
        students_dict[student_name].append(student_grade)

students_average_grades = {}

for student_name, student_grade in students_dict.items():
    average_grade = sum(student_grade) / len(student_grade)
    if average_grade >= 4.50:
        students_average_grades[student_name] = average_grade

sorted_students_average_grades = sorted(students_average_grades.items(), key=lambda x: -x[1])

for student_name, student_grade in sorted_students_average_grades:
    print(f"{student_name} -> {student_grade:.2f}")
