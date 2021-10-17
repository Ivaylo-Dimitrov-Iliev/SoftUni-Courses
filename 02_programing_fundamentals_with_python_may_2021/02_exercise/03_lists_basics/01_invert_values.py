string_of_numbers = input().split()

number_reversed = []

for number in string_of_numbers:
    current_number = int(number) * -1
    number_reversed.append(current_number)

print(number_reversed)
