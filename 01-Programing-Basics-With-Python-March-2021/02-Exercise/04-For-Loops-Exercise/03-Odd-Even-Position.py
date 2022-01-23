
import sys

# input

count_of_numbers = int(input())

# variables

odd_sum = 0
even_sum = 0

smallest_even_number = sys.maxsize
biggest_even_number = -sys.maxsize

smallest_odd_number = sys.maxsize
biggest_odd_number = -sys.maxsize

# loop

for sequence in range(1, count_of_numbers + 1,):
    current_number = float(input())
    if sequence % 2 == 0:
        even_sum += current_number
        if current_number < smallest_even_number:
            smallest_even_number = current_number
        if current_number > biggest_even_number:
            biggest_even_number = current_number
    elif sequence % 2 != 0:
        odd_sum += current_number
        if current_number < smallest_odd_number:
            smallest_odd_number = current_number
        if current_number > biggest_odd_number:
            biggest_odd_number = current_number

# output

print(f'OddSum={odd_sum:.2f},')

if smallest_odd_number == sys.maxsize:
    print('OddMin=No,')
else:
    print(f'OddMin={smallest_odd_number:.2f},')

if biggest_odd_number == -sys.maxsize:
    print('OddMax=No,')
else:
    print(f'OddMax={biggest_odd_number:.2f},')

print(f'EvenSum={even_sum:.2f},')

if smallest_even_number == sys.maxsize:
    print('EvenMin=No,')
else:
    print(f'EvenMin={smallest_even_number:.2f},')

if biggest_even_number == -sys.maxsize:
    print('EvenMax=No')
else:
    print(f'EvenMax={biggest_even_number:.2f}')
