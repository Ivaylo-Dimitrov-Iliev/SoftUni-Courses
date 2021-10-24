# input

name = input()
year_grade = 0

# variables

grade = 1
sum_of_year_grades = 0
failed_exam = 0

# loop

while grade <= 12:
    year_grade = float(input())
    if year_grade < 4.00:
        failed_exam += 1
        if failed_exam > 1:
            break
    sum_of_year_grades += year_grade
    grade += 1

# calculations

average_grade = sum_of_year_grades / (grade -1)

# output

if grade == 13:
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
else:
    print(f'{name} has been excluded at {(grade - 1)} grade')
