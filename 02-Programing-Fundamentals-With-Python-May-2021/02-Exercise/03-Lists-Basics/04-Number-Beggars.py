string_of_integers = input().split(", ")
count_of_beggars = int(input())

list_of_beggars_income = [0] * count_of_beggars
list_of_numbers = []

for element in string_of_integers:
    list_of_numbers.append(int(element))

for index in range(len(list_of_numbers)):
    current_position = index % count_of_beggars
    list_of_beggars_income[current_position] += list_of_numbers[index]

print(list_of_beggars_income)
