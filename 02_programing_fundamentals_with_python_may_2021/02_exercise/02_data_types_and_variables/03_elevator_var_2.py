number_of_people = int(input())
capacity_of_elevator = int(input())

number_of_courses = number_of_people // capacity_of_elevator

if not number_of_people % capacity_of_elevator == 0:
    number_of_courses += 1

print(number_of_courses)
