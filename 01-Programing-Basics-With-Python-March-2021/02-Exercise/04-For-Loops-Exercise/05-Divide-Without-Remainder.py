# input

count_of_numbers = int(input())

# variables - percentage groups

p1 = 0
p2 = 0
p3 = 0

# loop

for sequence in range(1, count_of_numbers + 1):
    value_of_number = int(input())
    if value_of_number % 2 == 0:
        p1 += 1
    if value_of_number % 3 == 0:
        p2 += 1
    if value_of_number % 4 == 0:
        p3 += 1

# percent calculations

p1 = p1 * 100 / count_of_numbers
p2 = p2 * 100 / count_of_numbers
p3 = p3 * 100 / count_of_numbers

# output

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
