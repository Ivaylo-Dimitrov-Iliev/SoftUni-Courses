employees_happiness = [int(el) for el in input().split()]
happiness_improvement_factor = int(input())

increased_employees_happiness = [el * happiness_improvement_factor for el in employees_happiness]

happiness_threshold = sum(increased_employees_happiness) / len(employees_happiness)

count_of_happy_employees = 0

happy_employees = [el for el in increased_employees_happiness if el >= happiness_threshold]
unhappy_employees = [el for el in increased_employees_happiness if el < happiness_threshold]

if len(happy_employees) >= len(unhappy_employees):
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employees_happiness)}. Employees are not happy!")
