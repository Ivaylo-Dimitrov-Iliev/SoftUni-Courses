def character_sequence(character_1, character_2):
    sequence_of_characters = ""
    for current_char in range(ord(character_1) + 1, ord(character_2)):
        current_symbol = chr(current_char)
        sequence_of_characters += current_symbol + " "
    return sequence_of_characters


char_1 = input()
char_2 = input()

print(character_sequence(char_1, char_2))
