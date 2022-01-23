import re

pattern = r"%(?P<name>[A-Z][a-z]+)%([^\|\$\%\.])*<(?P<product>\w+)>([^\|\$\%\.])*\|(?P<count>\d+)\|([^\d]*)(?P<price>\d+[\.\d+]*)\$"

order = input()

total_income = 0

while not order == "end of shift":
    valid_order = re.match(pattern, order)
    if valid_order is not None:
        customer_name = valid_order.group("name")
        product = valid_order.group("product")
        count = int(valid_order.group("count"))
        price = float(valid_order.group("price"))
        current_income = count * price
        total_income += current_income
        print(f"{customer_name}: {product} - {current_income:.2f}")

    order = input()

print(f"Total income: {total_income:.2f}")
