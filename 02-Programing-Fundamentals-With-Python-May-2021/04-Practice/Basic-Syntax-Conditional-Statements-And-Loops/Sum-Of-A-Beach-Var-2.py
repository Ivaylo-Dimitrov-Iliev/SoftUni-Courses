string = input()

new_string = string.lower()

substring_1 = "sand"
substring_2 = "water"
substring_3 = "fish"
substring_4 = "sun"

counter_1 = new_string.count(substring_1)
counter_2 = new_string.count(substring_2)
counter_3 = new_string.count(substring_3)
counter_4 = new_string.count(substring_4)

print(counter_1 + counter_2 + counter_3 + counter_4)
