string = input().split()

for word in string:
    for i in range(len(word)):
        if word[i] == ":":
            print(f"{word[i]}{word[i + 1]}")
