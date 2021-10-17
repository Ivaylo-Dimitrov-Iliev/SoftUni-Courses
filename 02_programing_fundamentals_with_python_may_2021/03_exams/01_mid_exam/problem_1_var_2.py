count_of_orders = int(input())

total_prise = 0

while not count_of_orders == 0:
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    price = ((days * capsule_count) * price_per_capsule)
    total_prise += price
    count_of_orders -= 1
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_prise:.2f}")
