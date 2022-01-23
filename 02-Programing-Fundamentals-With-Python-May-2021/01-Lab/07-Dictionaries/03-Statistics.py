command = input()

products = {}

while not command == "statistics":
    command_data_list = command.split(": ")
    key = command_data_list[0]
    value = int(command_data_list[1])
    if key in products:
        products[key] += value
    else:
        products[key] = value

    command = input()

print(f"Products in stock:")

for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
