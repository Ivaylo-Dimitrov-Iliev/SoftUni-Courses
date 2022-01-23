price_of_hall_rent = int(input())
cake_price = price_of_hall_rent * 0.2
drinks_price = cake_price - 0.45 * cake_price
animator_price = price_of_hall_rent / 3
total_price = price_of_hall_rent + cake_price + drinks_price + animator_price
print(total_price)
