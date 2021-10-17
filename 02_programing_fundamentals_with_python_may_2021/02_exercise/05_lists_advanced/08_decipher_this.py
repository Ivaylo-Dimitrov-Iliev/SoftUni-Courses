secret_message = input().split()

for current_word in secret_message:
    digits = ""
    letters = ""
    for el in current_word:
        if el.isdigit():
            digits += el
        else:
            letters += el
    first_letter = chr(int(digits))
    rest_letters_list = list(letters)
    rest_letters_list[0], rest_letters_list[-1] = rest_letters_list[-1], rest_letters_list[0]
    rest_letters = "".join(rest_letters_list)
    deciphered_word = first_letter + rest_letters
    print(deciphered_word, end=" ")