# input

product = input()
city = input()
quantity = float(input())

# variable

cost = 0

# statements

if city == 'Sofia':
    if product == 'coffee':
        cost = 0.5
    elif product == 'water':
        cost = 0.8
    elif product == 'beer':
        cost = 1.2
    elif product == 'sweets':
        cost = 1.45
    elif product == 'peanuts':
        cost = 1.6

elif city == 'Plovdiv':
    if product == 'coffee':
        cost = 0.4
    elif product == 'water':
        cost = 0.7
    elif product == 'beer':
        cost = 1.15
    elif product == 'sweets':
        cost = 1.3
    elif product == 'peanuts':
        cost = 1.5

elif city == 'Varna':
    if product == 'coffee':
        cost = 0.45
    elif product == 'water':
        cost = 0.7
    elif product == 'beer':
        cost = 1.1
    elif product == 'sweets':
        cost = 1.35
    elif product == 'peanuts':
        cost = 1.55

final_cost = cost * quantity

# output

print(final_cost)
