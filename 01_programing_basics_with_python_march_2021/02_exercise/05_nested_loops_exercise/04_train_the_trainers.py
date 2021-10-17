# input

count_jury = int(input())
presentation = input()

# variables

sum_all_grades = 0
count_all_grades = 0

# loop

while presentation != 'Finish':
    sum_grades = 0
    for juri in range(1, count_jury + 1):
        grade = float(input())
        sum_grades += grade
        sum_all_grades += grade
        count_all_grades += 1
    average_grade = sum_grades / count_jury
    print(f'{presentation} - {average_grade:.2f}.')
    presentation = input()

else:
    average_all = sum_all_grades / count_all_grades
    print(f'Student\'s final assessment is {average_all:.2f}.')
