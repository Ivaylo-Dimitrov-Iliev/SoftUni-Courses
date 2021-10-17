# input

count_of_numbers = int(input())

# variable

sum_of_numbers = 0

# loop

for row_of_numbers in range(1, count_of_numbers + 1):
    current_number = int(input())
    sum_of_numbers += current_number

print(sum_of_numbers)
