word = (input())

sequence_of_capital_letters = ""

for digit in word:
    if digit.isupper():
        sequence_of_capital_letters += digit



positions_of_capital_letters = sequence_of_capital_letters.index(1)

print(positions_of_capital_letters)
