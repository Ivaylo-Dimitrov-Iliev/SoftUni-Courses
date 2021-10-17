key = [el for el in input() if not el == " "]
key_str = "".join(key)

command = input()

while not command == "find":
    decrypted_message = ""
    i = 0

    while i in range(len(command)):
        for j in range(len(key_str)):
            char = chr(int(ord(command[i])) - int(key_str[j]))
            decrypted_message += char
            i += 1
            if i == len(command):
                break

    treasure_type = ""
    coordinates = ""
    i = 0
    while i in range(len(decrypted_message)):
        if decrypted_message[i] == "&":
            i += 1
            while not decrypted_message[i] == "&":
                treasure_type += decrypted_message[i]
                i += 1
        elif decrypted_message[i] == "<":
            i += 1
            while not decrypted_message[i] == ">":
                coordinates += decrypted_message[i]
                i += 1
        i += 1

    print(f"Found {treasure_type} at {coordinates}")

    command = input()
