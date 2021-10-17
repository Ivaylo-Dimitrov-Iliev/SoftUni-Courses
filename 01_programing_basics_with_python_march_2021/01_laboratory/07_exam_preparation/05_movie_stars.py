# input

budget = float(input())

# boolean variable

there_is_budget = True

# secondary input

command = input()

# loop

while command != 'ACTION':
    actor_name = command
    actor_salary = 0
    if len(actor_name) > 15:
        actor_salary = budget * 0.20
    else:
        actor_salary = float(input())
    budget -= actor_salary
    if budget < 0:
        there_is_budget = False
        break
    command = input()

# output

if there_is_budget:
    print(f'We are left with {budget:.2f} leva.')
else:
    print(f'We need {abs(budget):.2f} leva for our actors.')
