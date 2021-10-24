import sys

min_number = sys.maxsize

# input

command = input()

# loop

while command != 'Stop':
    current_number = int(command)
    if current_number < min_number:
        min_number = current_number
    command = input()

# output

print(min_number)
