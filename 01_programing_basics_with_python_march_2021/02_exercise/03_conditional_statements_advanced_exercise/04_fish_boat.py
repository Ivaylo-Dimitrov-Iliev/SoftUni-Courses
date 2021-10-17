# input

budget = int(input())
season = input()
fishers = int(input())

# variable

final_price = 0

# statements

if season == "Spring":
    final_price = 3000

elif season == "Summer" or season == "Autumn":
    final_price = 4200

elif season == "Winter":
    final_price = 2600

# discount 1

if fishers <= 6:
    final_price *= 0.9
elif 7 < fishers <= 11:
    final_price *= 0.85
elif fishers >= 12:
    final_price *= 0.75

# discount 2

if (not season == "Autumn") and fishers % 2 == 0:
    final_price *= 0.95

if budget >= final_price:
    left_money = budget - final_price
    print(f"Yes! You have {left_money:.2f} leva left.")
else:
    need_money = final_price - budget
    print(f"Not enough money! You need {need_money:.2f} leva.")
