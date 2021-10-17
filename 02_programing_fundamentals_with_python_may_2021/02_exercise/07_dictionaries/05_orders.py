product = input()

products_dict = {}

while not product == "buy":
    data_list = product.split()
    name, price, quantity = data_list
    if name not in products_dict:
        products_dict[name] = [float(price), int(quantity)]
    else:
        products_dict[name][1] += int(quantity)
        products_dict[name][0] = float(price)

    product = input()
[print(f"{key} -> {value[0] * value[1]:.2f}") for key, value in products_dict.items()]
