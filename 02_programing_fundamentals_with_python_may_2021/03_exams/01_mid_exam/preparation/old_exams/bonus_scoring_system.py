import math

count_of_students = int(input())
count_of_the_lectures = int(input())
additional_bonus = int(input())

max_bonus = 0
attendances = 0

while count_of_students > 0:
    count_of_attendances = int(input())
    bonus = count_of_attendances / count_of_the_lectures * (5 + additional_bonus)
    if max_bonus < bonus:
        max_bonus = bonus
        attendances = count_of_attendances
    count_of_students -= 1

print(f"Max Bonus: {math.ceil(max_bonus)}.")
print(f"The student has attended {attendances} lectures.")
