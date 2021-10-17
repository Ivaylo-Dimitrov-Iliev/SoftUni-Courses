# input

drinks_type = input()
sugar = input()
number_of_drinks = int(input())

# variable

drink_price = 0

# loop

if drinks_type == 'Espresso':
    if sugar == 'Without':
        drink_price = 0.90
        drink_price *= 0.65
    elif sugar == 'Normal':
        drink_price = 1
    elif sugar == 'Extra':
        drink_price = 1.20
    if number_of_drinks >= 5:
        drink_price *= 0.75
elif drinks_type == 'Cappuccino':
    if sugar == 'Without':
        drink_price = 1
        drink_price *= 0.65
    elif sugar == 'Normal':
        drink_price = 1.20
    elif sugar == 'Extra':
        drink_price = 1.60
elif drinks_type == 'Tea':
    if sugar == 'Without':
        drink_price = 0.50
        drink_price *= 0.65
    elif sugar == 'Normal':
        drink_price = 0.60
    elif sugar == 'Extra':
        drink_price = 0.70

# variable

total_sum = drink_price * number_of_drinks

# discount loop

if total_sum > 15:
    total_sum *= 0.8

# output

print(f'You bought {number_of_drinks} cups of {drinks_type} for {total_sum:.2f} lv.')