import re

pattern = r"\d+"

text = input()

while not text == "":
    is_digit = False
    for el in text:
        if el.isdigit():
            is_digit = True
            break
    if is_digit:
        numbers = re.findall(pattern, text)
        print(*numbers, end=" ")
    text = input()
