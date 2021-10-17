# input

destination = input()
needed_budget = float(input())

# variable

total_saved_money = 0

# loop

while destination != 'End':
    while total_saved_money < needed_budget:
        saved_money = float(input())
        total_saved_money += saved_money
    else:
        total_saved_money = 0
        print(f'Going to {destination}!')

    destination = input()

    if destination != 'End':
        needed_budget = float(input())
