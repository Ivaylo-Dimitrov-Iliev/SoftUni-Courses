#inputs

price_of_strawberries = float(input())
quantity_of_bananas_in_kg = float(input())
quantity_of_oranges_in_kg = float(input())
quantity_of_raspberries_in_kg = float(input())
quantity_of_strawberries_in_kg = float(input())

#prices

price_of_raspberries = price_of_strawberries * 0.5
price_of_oranges = price_of_raspberries - price_of_raspberries * 0.4
price_of_bananas = price_of_raspberries - price_of_raspberries * 0.8

#costs

cost_for_strawberries = price_of_strawberries * quantity_of_strawberries_in_kg
cost_for_bananas = price_of_bananas * quantity_of_bananas_in_kg
cost_for_oranges = price_of_oranges * quantity_of_oranges_in_kg
cost_for_raspberries = price_of_raspberries * quantity_of_raspberries_in_kg

#total_cost

total_cost = cost_for_strawberries + cost_for_bananas + cost_for_oranges + cost_for_raspberries

#output

print(total_cost)
