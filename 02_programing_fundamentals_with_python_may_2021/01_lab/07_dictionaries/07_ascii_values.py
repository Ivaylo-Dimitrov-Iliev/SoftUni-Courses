list_of_characters = input().split(", ")

ascii_characters = {el: ord(el) for el in list_of_characters}

print(ascii_characters)