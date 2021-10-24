import sys

max_number = -sys.maxsize

# input

command = input()

# loop

while command != 'Stop':
    current_number = int(command)
    if current_number > max_number:
        max_number = current_number
    command = input()

# output

print(max_number)
