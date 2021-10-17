string = input()

command = input()

while not command == "Done":
    data = command.split()
    action = data[0]
    if action == "TakeOdd":
        temporary_string = ""
        for i in range(len(string)):
            if i % 2 == 1:
                temporary_string += string[i]
        string = temporary_string
        print(string)

    elif action == "Cut":
        index = int(data[1])
        length = int(data[2])
        substring = string[index:index + length]
        string = string.replace(substring, "", 1)
        print(string)

    elif action == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in string:
            string = string.replace(substring, substitute)
            print(string)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {string}")
