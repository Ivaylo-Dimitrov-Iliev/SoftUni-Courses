n = int(input())

for _ in range(n):
    text = input()
    name = ""
    age = ""
    for i in range(len(text)):
        if text[i] == "@":
            i += 1
            while not text[i] == "|":
                name += text[i]
                i += 1
        elif text[i] == "#":
            i += 1
            while not text[i] == "*":
                age += text[i]
                i += 1
    print(f"{name} is {age} years old.")
