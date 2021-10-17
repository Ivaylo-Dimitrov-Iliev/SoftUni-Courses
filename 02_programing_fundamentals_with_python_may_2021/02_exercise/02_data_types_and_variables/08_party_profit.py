import math

party_size = int(input())
days = int(input())

total_coins = 0
companions_count = party_size

for current_day in range(1, days + 1):
    if current_day % 10 == 0:
        companions_count -= 2
    if current_day % 15 == 0:
        companions_count += 5
    total_coins += 50
    total_coins -= 2 * companions_count
    if current_day % 3 == 0:
        total_coins -= 3 * companions_count
    if current_day % 5 == 0:
        total_coins += 20 * companions_count
        if current_day % 3 == 0:
            total_coins -= 2 * companions_count

profit_per_companion = math.floor(total_coins / companions_count)

print(f"{companions_count} companions received {profit_per_companion} coins each.")
