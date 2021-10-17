def total_price(product, quantity):
    if product == "coffee":
        result = quantity * 1.50
    elif product == "water":
        result = quantity
    elif product == "coke":
        result = quantity * 1.40
    elif product == "snacks":
        result = quantity * 2.00
    return result


goods = input()
count_of_goods = int(input())

print(f"{total_price(goods, count_of_goods):.2f}")
