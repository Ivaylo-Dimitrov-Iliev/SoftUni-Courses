count_of_numbers = int(input())

list_of_even_numbers = []
list_of_odd_numbers = []
list_of_negative_numbers = []
list_of_positive_numbers = []

for _ in range(1, count_of_numbers + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        list_of_even_numbers.append(current_number)
    if current_number % 2 == 1:
        list_of_odd_numbers.append(current_number)
    if current_number < 0:
        list_of_negative_numbers.append(current_number)
    if current_number >= 0:
        list_of_positive_numbers.append(current_number)

key_word = input()

if key_word == "even":
    print(list_of_even_numbers)
elif key_word == "odd":
    print(list_of_odd_numbers)
elif key_word == "negative":
    print(list_of_negative_numbers)
elif key_word == "positive":
    print(list_of_positive_numbers)
