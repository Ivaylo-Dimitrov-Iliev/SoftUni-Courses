command = input()

companies = {}

while not command == "End":
    data = command.split(" -> ")
    company_name, employees_id = data
    if company_name not in companies:
        companies[company_name] = [employees_id]
    else:
        if employees_id not in companies[company_name]:
            companies[company_name].append(employees_id)
    command = input()

sorted_companies = sorted(companies.items(), key=lambda x: x[0])

for company_name, employees_id in sorted_companies:
    print(company_name)
    [print(f"-- {el}") for el in employees_id]