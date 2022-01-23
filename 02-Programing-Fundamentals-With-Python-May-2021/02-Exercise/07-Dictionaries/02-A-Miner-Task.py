resource = input()
if not resource == "stop":
    quantity = int(input())

resources_dict = {}

while not resource == "stop":
    if resource not in resources_dict:
        resources_dict[resource] = 0
    resources_dict[resource] += quantity
    resource = input()
    if not resource == "stop":
        quantity = int(input())

for resource, quantity in resources_dict.items():
    print(f"{resource} -> {quantity}")
