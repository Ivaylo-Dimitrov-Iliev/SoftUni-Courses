list_of_numbers = input().split(", ")

print([index for index in range(len(list_of_numbers)) if int(list_of_numbers[index]) % 2 == 0])
