message = input()
command = input()

while not command == "Reveal":
    data = command.split(":|:")
    action = data[0]

    if action == "InsertSpace":
        index = int(data[1])
        first_half = message[:index]
        second_half = message[index:]
        message = first_half + " " + second_half

    elif action == "Reverse":
        substring = data[1]
        reversed_substring = substring[::-1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += reversed_substring
        else:
            print("error")
            command = input()
            continue

    elif action == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)

    print(message)
    command = input()

print(f"You have a new text message: {message}")
