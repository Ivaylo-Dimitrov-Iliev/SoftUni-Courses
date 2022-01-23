count_of_numbers = int(input())

list_of_positive_numbers = []
list_negative_numbers = []

for numbers in range(1, count_of_numbers + 1):
    current_number = int(input())
    if current_number >= 0:
        list_of_positive_numbers.append(current_number)
    else:
        list_negative_numbers.append(current_number)

print(list_of_positive_numbers)
print(list_negative_numbers)
print(f"Count of positives: {len(list_of_positive_numbers)}. Sum of negatives: {sum(list_negative_numbers)}")
