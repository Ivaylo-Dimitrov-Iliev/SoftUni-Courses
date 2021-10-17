
import sys

# input

number = int(input())

# variable

max_value = -sys.maxsize

sum_of_values = 0

# loop

for number in range(1, number +1):
    value = int(input())
    if value > max_value:
        max_value = value
    sum_of_values += value

# variable

sum_of_rest_values = sum_of_values - max_value

# conditional statement

if max_value == sum_of_rest_values:
    print('Yes')
    print(f'Sum = {max_value}')
else:
    diff = abs(max_value - sum_of_rest_values)
    print('No')
    print(f'Diff = {diff}')
