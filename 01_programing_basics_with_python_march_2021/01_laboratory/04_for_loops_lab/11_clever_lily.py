# input

age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

# variables

birthday_money = 0
total_money = 0
total_toys = 0

# loop

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        birthday_money += 10
        total_money += birthday_money -1
    else:
        total_toys += 1

# new variables10

toys_money = total_toys * toy_price
total_money += toys_money
difference = abs(total_money - washing_machine_price)

# output

if total_money >= washing_machine_price:
    print(f'Yes! {difference:.2f}')
else:
    print(f'No! {difference:.2f}')
