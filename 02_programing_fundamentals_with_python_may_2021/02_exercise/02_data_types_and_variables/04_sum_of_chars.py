count_of_characters = int(input())

total_sum_of_character_ascii_values = 0

while count_of_characters > 0:
    new_character = input()
    total_sum_of_character_ascii_values += ord(new_character)
    count_of_characters -= 1

print(f"The sum equals: {total_sum_of_character_ascii_values}")
