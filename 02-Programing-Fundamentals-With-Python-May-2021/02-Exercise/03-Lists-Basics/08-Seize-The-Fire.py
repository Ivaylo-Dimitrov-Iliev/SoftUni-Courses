type_of_fires_and_level_of_their_cells = input().split("#")
amount_of_water = int(input())

total_effort = 0
total_fire = 0
list_of_extinguished_fires = []

for current_fire in type_of_fires_and_level_of_their_cells:
    current_fire_as_string = str(current_fire)
    current_fire_data_list = current_fire_as_string.split(" = ")
    if current_fire_data_list[0] == "High":
        if 80 < int(current_fire_data_list[1]) <= 125:
            if amount_of_water >= int(current_fire_data_list[1]):
                amount_of_water -= int(current_fire_data_list[1])
                current_effort = int(current_fire_data_list[1]) * 0.25
                total_effort += current_effort
                total_fire += int(current_fire_data_list[1])
                list_of_extinguished_fires.append(current_fire_data_list[1])
            else:
                pass
        else:
            pass
    elif current_fire_data_list[0] == "Medium":
        if 50 < int(current_fire_data_list[1]) <= 80:
            if amount_of_water >= int(current_fire_data_list[1]):
                amount_of_water -= int(current_fire_data_list[1])
                current_effort = int(current_fire_data_list[1]) * 0.25
                total_effort += current_effort
                total_fire += int(current_fire_data_list[1])
                list_of_extinguished_fires.append(current_fire_data_list[1])
            else:
                pass
        else:
            pass
    elif current_fire_data_list[0] == "Low":
        if 0 < int(current_fire_data_list[1]) <= 50:
            if amount_of_water >= int(current_fire_data_list[1]):
                amount_of_water -= int(current_fire_data_list[1])
                current_effort = int(current_fire_data_list[1]) * 0.25
                total_effort += current_effort
                total_fire += int(current_fire_data_list[1])
                list_of_extinguished_fires.append(current_fire_data_list[1])
            else:
                pass
        else:
            pass

list_of_extinguished_fires.insert(0, "Cells:")

print('\n - '.join(list_of_extinguished_fires))
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
