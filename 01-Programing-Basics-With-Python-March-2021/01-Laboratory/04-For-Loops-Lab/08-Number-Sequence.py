import sys

smallest_number = sys.maxsize
biggest_number = -sys.maxsize

# input

count_of_numbers = int(input())

# loop

for count in range(1, count_of_numbers + 1):
    current_number = int(input())
    if current_number < smallest_number:
        smallest_number = current_number
    if current_number > biggest_number:
        biggest_number = current_number

# output

print(f'Max number: {biggest_number}')
print(f'Min number: {smallest_number}')
