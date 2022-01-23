count_of_numbers = int(input())

list_numbers = []
list_filtered_numbers = []

for _ in range(1, count_of_numbers + 1):
    number = int(input())
    list_numbers.append(number)

command = input()

if command == "even":
    for current_number in list_numbers:
        if current_number % 2 == 0:
            list_filtered_numbers.append(current_number)
elif command == "odd":
    for current_number in list_numbers:
        if current_number % 2 == 1:
            list_filtered_numbers.append(current_number)
elif command == "negative":
    for current_number in list_numbers:
        if current_number < 0:
            list_filtered_numbers.append(current_number)
elif command == "positive":
    for current_number in list_numbers:
        if current_number >= 0:
            list_filtered_numbers.append(current_number)

print(list_filtered_numbers)
