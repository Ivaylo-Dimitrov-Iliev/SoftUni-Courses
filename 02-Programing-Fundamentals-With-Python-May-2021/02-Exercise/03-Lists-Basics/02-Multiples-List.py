factor_number = int(input())
count_number = int(input())

list_of_numbers = []
start_number = 0

for number in range(1, count_number + 1):
    start_number += factor_number
    list_of_numbers.append(start_number)

print(list_of_numbers)
