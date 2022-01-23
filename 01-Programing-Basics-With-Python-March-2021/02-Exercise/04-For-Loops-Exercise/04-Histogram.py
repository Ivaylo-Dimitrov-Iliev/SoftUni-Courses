# input

count_of_numbers = int(input())

# variables - percentage groups

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

# loop

for sequence in range(1, count_of_numbers + 1):
    value_of_number = int(input())
    if value_of_number < 200:
        p1 += 1
    elif 200 <= value_of_number < 400:
        p2 += 1
    elif 400 <= value_of_number < 600:
        p3 += 1
    elif 600 <= value_of_number < 800:
        p4 += 1
    elif value_of_number >= 800:
        p5 += 1

# percent calculations

p1 = p1 * 100 / count_of_numbers
p2 = p2 * 100 / count_of_numbers
p3 = p3 * 100 / count_of_numbers
p4 = p4 * 100 / count_of_numbers
p5 = p5 * 100 / count_of_numbers

# output

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
