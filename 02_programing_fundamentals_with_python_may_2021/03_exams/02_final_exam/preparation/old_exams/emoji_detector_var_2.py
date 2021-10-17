import re

emojis_pattern = r"(?P<surrounding>\:\:|\*\*)(?P<name>[A-z][a-z]{2,})(?P=surrounding)"
digits_pattern = r"\d"

text = input()

emoji_matches = re.finditer(emojis_pattern, text)
digits_matches = re.findall(digits_pattern, text)

cool_threshold = 1
cool_emojis = []

for match in digits_matches:
    cool_threshold *= int(match)

print(f"Cool threshold: {cool_threshold}")

emoji_count = 0

for match in emoji_matches:
    emoji_count += 1
    data = match.groupdict()
    name = data["name"]
    coolness = sum([ord(el) for el in name])
    if coolness >= cool_threshold:
        cool_emojis.append(f"{data['surrounding']}{data['name']}{data['surrounding']}")

print(f"{emoji_count} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)
