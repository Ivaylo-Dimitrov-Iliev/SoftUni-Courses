str_of_numbers = input().split()
count_of_numbers_to_remove = int(input())

numbers = []

for el in str_of_numbers:
    numbers.append(int(el))

for _ in range(1, count_of_numbers_to_remove + 1):
    numbers.remove(min(numbers))

new_list_of_string_numbers = []

for element in numbers:
    new_list_of_string_numbers.append(str(element))

numbers_left = ", ".join(new_list_of_string_numbers)

print(numbers_left)

