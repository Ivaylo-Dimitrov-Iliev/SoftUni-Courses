# input

count_of_open_tabs = int(input())
salary = int(input())

# loop

for sequence in range(1, count_of_open_tabs + 1):
    tab = input('')
    if tab == 'Facebook':
        salary -= 150
    elif tab == 'Instagram':
        salary -= 100
    elif tab == 'Reddit':
        salary -= 50
    else:
        salary -= 0

    if salary <= 0:
        print('You have lost your salary.')
        break

if salary > 0:
    print(salary)
