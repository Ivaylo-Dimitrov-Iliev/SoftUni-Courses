#input

vacation_cost = float(input())
number_of_puzzles = int(input())
number_of_speaking_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

#toys_prices

puzzle_price = 2.6
speaking_doll_price = 3
teddy_bear_price = 4.1
minion_price = 8.2
truck_price = 2

#calculations

total_toys_income = number_of_puzzles * puzzle_price + number_of_speaking_dolls * speaking_doll_price + number_of_teddy_bears * teddy_bear_price\
                    + number_of_minions * minion_price + number_of_trucks * truck_price

total_number_of_toys = number_of_puzzles + number_of_speaking_dolls + number_of_teddy_bears + number_of_minions + number_of_trucks

if total_number_of_toys >= 50:
    total_toys_income *= 0.75

total_toys_income *= 0.9

difference = abs(total_toys_income - vacation_cost)

#output

if total_toys_income >= vacation_cost:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")