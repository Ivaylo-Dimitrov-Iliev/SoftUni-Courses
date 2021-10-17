import re

text = input()

pattern = r"(?P<surr>\@|\#)(?P<word_1>[A-Za-z]{3,})(?P=surr)(?P=surr)(?P<word_2>[A-Za-z]{3,})(?P=surr)"

matches = re.finditer(pattern, text)

pair_words = 0
mirror_words = []

for match in matches:
    pair_words += 1
    data = match.groupdict()
    word_1 = data["word_1"]
    word_2 = data["word_2"]
    reversed_word_2 = word_2[::-1]
    if word_1 == reversed_word_2:
        mirror_words.append(f"{word_1} <=> {word_2}")

if pair_words == 0:
    print("No word pairs found!")
else:
    print(f"{pair_words} word pairs found!")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print(f"The mirror words are:")
    print(', '.join(mirror_words))