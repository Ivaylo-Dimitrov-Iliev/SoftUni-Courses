number_of_fill_ups = int(input())

current_level_of_tank = 0

tank_is_full = False

for level in range(number_of_fill_ups):
    current_fill_up = int(input())
    if current_level_of_tank <= 255:
        current_level_of_tank += current_fill_up
    if current_level_of_tank > 255:
        current_level_of_tank -= current_fill_up
        tank_is_full = True

if tank_is_full:
    print("Insufficient capacity!")

print(current_level_of_tank)
