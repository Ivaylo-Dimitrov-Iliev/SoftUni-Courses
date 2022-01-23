input_text = input()

vowels = ['a', 'o', 'u', 'e', 'i']

print("".join([el for el in input_text if not el.lower() in vowels]))
