key = [el for el in input() if not el == " "]
key_str = "".join(key)

command = input()

while not command == "find":
    location = ""
    for el, num in zip(command, key_str):
        el = chr(int(ord(el)) - int(num))
        location += el
        if key_str.index(num) == len(key_str) - 1:
            num = key_str[0]
    print(location)
    command = input()
