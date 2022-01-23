import re

emojis_pattern = r"(?P<emoji>(?P<surrounding>\:\:|\*\*)(?P<name>[A-z][a-z]{2,})(?P=surrounding))"
digits_pattern = r"\d"

text = input()

valid_emojis = []
cool_threshold = 1
cool_emojis = []

emoji_matches = re.finditer(emojis_pattern, text)
digits_matches = re.findall(digits_pattern, text)

for match in digits_matches:
    cool_threshold *= int(match)

for match in emoji_matches:
    valid_emojis.append(match.group("emoji"))

for emoji in valid_emojis:
    coolness = 0
    for el in emoji:
        if el.isalpha():
            coolness += ord(el)
    if coolness >= cool_threshold:
        cool_emojis.append(emoji)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)
