string = input()

word_1 = "sand"
word_2 = "water"
word_3 = "fish"
word_4 = "sun"

counter = 0

new_string = string.lower()

if word_1 in new_string:
    counter += 1
if word_2 in new_string:
    counter += 1
if word_3 in new_string:
    counter += 1
if word_4 in new_string:
    counter += 1

print(counter)
