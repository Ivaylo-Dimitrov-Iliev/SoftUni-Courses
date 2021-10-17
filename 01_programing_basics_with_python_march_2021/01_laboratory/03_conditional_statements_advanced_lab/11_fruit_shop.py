# input

fruit = input()
day = input()
quantity = float(input())

# variable

cost = 0

# statements

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        cost = 2.50
    elif fruit == 'apple':
        cost = 1.20
    elif fruit == 'orange':
        cost = 0.85
    elif fruit == 'grapefruit':
        cost = 1.45
    elif fruit == 'kiwi':
        cost = 2.70
    elif fruit == 'pineapple':
        cost = 5.50
    elif fruit == 'grapes':
        cost = 3.85

elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        cost = 2.70
    elif fruit == 'apple':
        cost = 1.25
    elif fruit == 'orange':
        cost = 0.90
    elif fruit == 'grapefruit':
        cost = 1.60
    elif fruit == 'kiwi':
        cost = 3.00
    elif fruit == 'pineapple':
        cost = 5.60
    elif fruit == 'grapes':
        cost = 4.20

# variable

total_cost = quantity * cost

# output
if cost != 0:
    print(f'{total_cost:.2f}')
else:
    print('error')
