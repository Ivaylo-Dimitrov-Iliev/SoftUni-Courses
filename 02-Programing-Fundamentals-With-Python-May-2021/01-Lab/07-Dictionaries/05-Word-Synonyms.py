number_of_words = int(input())

words = {}

for x in range (number_of_words):
    word = input()
    synonym = input()
    if word not in words:
        words[word] = []
    words[word].append(synonym)

for key in words:
    print(f"{key} - {', '.join(words[key])}")
