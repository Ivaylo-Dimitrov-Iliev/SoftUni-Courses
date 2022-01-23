# input

n = int(input())

# loop

for number in range(1111, 10000):
    units = number % 10
    tens = number // 10 % 10
    hundreds = number // 100 % 10
    thousands = number // 1000
    if n % units == 0 and n % tens == 0 and n % hundreds == 0 and n % thousands == 0:
        print(number)
