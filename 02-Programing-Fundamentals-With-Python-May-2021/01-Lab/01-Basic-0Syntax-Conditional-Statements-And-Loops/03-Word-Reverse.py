# input

word = input()

# variable

reversed_word = ""

# loop

for index in range(len(word) - 1, - 1, - 1):
    reversed_word += word[index]
print(reversed_word, end="")
