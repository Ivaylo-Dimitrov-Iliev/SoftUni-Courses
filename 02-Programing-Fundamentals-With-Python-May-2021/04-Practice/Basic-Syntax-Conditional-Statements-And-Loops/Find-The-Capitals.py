word = list(input())

list_of_capital_positions = []

for digit in range(len(word)):
    if word[digit].isupper():
        list_of_capital_positions.append(digit)

print(list_of_capital_positions)
