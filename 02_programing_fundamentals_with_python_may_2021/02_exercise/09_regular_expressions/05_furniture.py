import re

text = input()

pattern = r"^>>(?P<name>[A-Za-z]+)<<(?P<price>\d+([\.\d+]*))!(?P<quantity>\d+)$"

bought_furniture = []
total_cost = 0

while not text == "Purchase":
    match = re.match(pattern, text)
    if match is not None:
        name = match.group("name")
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        bought_furniture.append(name)
        total_cost += price * quantity
    text = input()

print("Bought furniture:")
for el in bought_furniture:
    print(el)
print(f"Total money spend: {total_cost:.2f}")
