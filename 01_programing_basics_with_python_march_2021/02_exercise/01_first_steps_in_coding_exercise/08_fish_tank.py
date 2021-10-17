#input

aquarium_length_in_cm = int(input())
aquarium_width_in_cm = int(input())
aquarium_hight_in_cm = int(input())
percentage_occupied_volume = float(input())

#calculations

total_volume_of_aqarium_in_cm3 = aquarium_length_in_cm * aquarium_width_in_cm * aquarium_hight_in_cm
total_volume_of_aqarium_in_l = total_volume_of_aqarium_in_cm3 * 0.001
percentage_transitioning = percentage_occupied_volume * 0.01
liters_of_water_required_for_aquarium_filling = total_volume_of_aqarium_in_l * (1 - percentage_transitioning)

#result

print(liters_of_water_required_for_aquarium_filling)
