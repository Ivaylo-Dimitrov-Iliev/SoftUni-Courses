collection_of_items = input().split("|")
budget = float(input())

list_of_items_new_prices = []
total_profit = 0
new_budget = 0
needed_budget = 150

for current_item in collection_of_items:
    current_item_info_list = current_item.split("->")
    item = current_item_info_list[0]
    item_price = float(current_item_info_list[1])
    if item == "Clothes" and item_price <= 50.00 and item_price <= budget:
        budget -= item_price
        item_new_price = item_price * 1.40
        current_profit = item_price * 0.40
        list_of_items_new_prices.append(item_new_price)
        total_profit += current_profit
    elif item == "Shoes" and item_price <= 35.00 and item_price <= budget:
        budget -= item_price
        item_new_price = item_price * 1.40
        current_profit = item_price * 0.40
        list_of_items_new_prices.append(item_new_price)
        total_profit += current_profit
    elif item == "Accessories" and item_price <= 20.50 and item_price <= budget:
        budget -= item_price
        item_new_price = item_price * 1.40
        current_profit = item_price * 0.40
        list_of_items_new_prices.append(item_new_price)
        total_profit += current_profit

for current_price in list_of_items_new_prices:
    new_budget += current_price

total_new_budget = new_budget + budget

if total_new_budget >= needed_budget:
    for current_price in list_of_items_new_prices:
        print(f"{current_price:.2f}", end=' ')
    print(f"\nProfit: {total_profit:.2f}")
    print("Hello, France!")
else:
    for current_price in list_of_items_new_prices:
        print(f"{current_price:.2f}", end=' ')
    print(f"\nProfit: {total_profit:.2f}")
    print("Time to go.")
