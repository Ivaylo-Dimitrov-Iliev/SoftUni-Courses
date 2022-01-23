# input

n = int(input())
l = int(input())

# loop

for first_digit in range(1, n):
    for second_digit in range(1, n):
        for third_digit in range(1, l + 1):
            third_digit = chr(third_digit + 96)
            for forth_digit in range(1, l + 1):
                forth_digit = chr(forth_digit + 96)
                for fifth_digit in range(1, n):
                    digit5 = fifth_digit + 1
                    while digit5 <= first_digit or digit5 <= second_digit:
                        digit5 += 1
                    print(f'{first_digit}{second_digit}{third_digit}{forth_digit}{digit5}', end=' ')
