count_of_courses = int(input())

list_of_courses = []

for courses in range(1, count_of_courses + 1):
    current_course = input()
    list_of_courses.append(current_course)

print(list_of_courses)
