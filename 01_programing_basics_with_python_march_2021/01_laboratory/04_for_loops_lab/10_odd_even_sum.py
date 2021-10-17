# input

count_of_numbers = int(input())

# var

odd_sum = 0
even_sum = 0

# loop

for number in range(1, count_of_numbers + 1):
    current_number = int(input())
    if number % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

#

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    difference = abs(even_sum - odd_sum)
    print('No')
    print(f'Diff = {difference}')
