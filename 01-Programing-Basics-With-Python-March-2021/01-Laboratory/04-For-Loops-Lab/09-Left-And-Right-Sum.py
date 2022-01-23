# input

count_of_numbers = int(input())

# variables

left_sum = 0
right_sum = 0

# loop for left sum

for sequence in range(1, count_of_numbers + 1):
    left_sum += int(input())

# conditional statement and check for right sum

if count_of_numbers < 2:
    for sequence in range(2, 2 * count_of_numbers + 1):
        right_sum += int(input())
else:
    for sequence in range(count_of_numbers + 1, 2 * count_of_numbers + 1):
        right_sum += int(input())

if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diff = abs(left_sum - right_sum)
    print(f'No, diff = {diff}')
