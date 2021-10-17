command = input()

courses_dict = {}

while not command == "end":
    data_list = command.split(" : ")
    course_name, student_name = data_list
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)
    command = input()

sorted_courses_dict = sorted(courses_dict.items(), key=lambda x: -len(x[1]))

for course_name, student_name in sorted_courses_dict:
    print(f"{course_name}: {len(student_name)}")
    student = sorted(student_name)
    [print(f"-- {el}") for el in student]