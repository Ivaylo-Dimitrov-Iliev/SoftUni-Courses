# input

width = int(input())
length = int(input())
height = int(input())

# calculations

total_volume = width * length * height

# boolean variable

there_is_more_free_space = True

# input

command = input()

# loop

while command != 'Done':
    number_of_boxes = int(command)
    total_volume -= number_of_boxes
    if total_volume < 0:
        there_is_more_free_space = False
        break
    command = input()

# output

if there_is_more_free_space:  # if there is more free space == True
    print(f'{total_volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(total_volume)} Cubic meters more.')
