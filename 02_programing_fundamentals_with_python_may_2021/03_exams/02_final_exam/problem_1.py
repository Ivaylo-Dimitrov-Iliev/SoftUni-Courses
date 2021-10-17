string = input()

command = input()

while not command == "Finish":
    data = command.split()
    action = data[0]

    if action == "Replace":
        current_char = data[1]
        new_char = data[2]
        string = string.replace(current_char, new_char)
        print(string)

    elif action == "Cut":
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index not in range(len(string)) or end_index not in range(len(string)):
            print("Invalid indices!")
        else:
            substring = string[start_index:end_index + 1]
            string = string.replace(substring, "")
            print(string)

    elif action == "Make":
        change_type = data[1]
        if change_type == "Upper":
            string = string.upper()
            print(string)
        elif change_type == "Lower":
            string = string.lower()
            print(string)

    elif action == "Check":
        substring = data[1]
        if substring in string:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif action == "Sum":
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index not in range(len(string)) or end_index not in range(len(string)):
            print("Invalid indices!")
        else:
            substring = string[start_index:end_index + 1]
            sum_ascii_values = 0
            for el in substring:
                sum_ascii_values += int(ord(el))
            print(sum_ascii_values)

    command = input()
