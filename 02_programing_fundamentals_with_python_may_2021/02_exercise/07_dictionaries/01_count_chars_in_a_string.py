characters = input().split()

characters_dict = {}

for el in characters:
    for char in el:
        if char not in characters_dict:
            characters_dict[char] = 0
        characters_dict[char] += 1

for char, count in characters_dict.items():
    print(f"{char} -> {count}")
