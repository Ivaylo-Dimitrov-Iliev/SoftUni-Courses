import re

text = input().lower()
word = input().lower()

pattern = rf"\b{word}\b"

count_of_word = re.findall(pattern, text).count(word)

print(count_of_word)
