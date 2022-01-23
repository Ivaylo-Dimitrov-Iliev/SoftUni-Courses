#input

movie_budget = float(input())
count_of_extras = int(input())
price_of_clothing_of_one_extra = float(input())

#calculations

decor_price = movie_budget * 0.1
expenses_for_clothing = count_of_extras * price_of_clothing_of_one_extra

if count_of_extras > 150:
    expenses_for_clothing = expenses_for_clothing * 0.9

movie_cost = decor_price + expenses_for_clothing

final_result = abs(movie_budget - movie_cost)

#output

if movie_budget < movie_cost:
    print("Not enough money!")
    print(f"Wingard needs {final_result:.2f} leva more.")
elif movie_budget >= movie_cost:
    print("Action!")
    print(f"Wingard starts filming with {final_result:.2f} leva left.")
