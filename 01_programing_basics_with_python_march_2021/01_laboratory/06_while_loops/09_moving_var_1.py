# input

apartment_width = int(input())
apartment_length = int(input())
apartment_height = int(input())
command = input()

# calculations

apartment_total_space = apartment_width * apartment_length * apartment_height

# variable

occupied_space = 0

# loop

while command != 'Done':
    current_number_boxes = int(command)
    occupied_space += current_number_boxes
    if apartment_total_space <= occupied_space:
        break
    command = input()

# calculations

diff_space = abs(apartment_total_space - occupied_space)

# output

if apartment_total_space > occupied_space:
    print(f'{diff_space} Cubic meters left.')
else:
    print(f'No more free space! You need {diff_space} Cubic meters more.')
