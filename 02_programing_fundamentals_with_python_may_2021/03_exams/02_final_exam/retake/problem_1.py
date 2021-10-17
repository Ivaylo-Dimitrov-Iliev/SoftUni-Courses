email = input()

command = input()

while not command == "Valid":
    data = command.split()
    action = data[0]

    if action == "Upper":
        index = int(data[1])
        old_char = email[index]
        new_char = email[index].upper()
        email = email.replace(old_char, new_char, 1)
        print(email)

    elif action == "Lower":
        index = int(data[1])
        old_char = email[index]
        new_char = email[index].lower()
        email = email.replace(old_char, new_char, 1)
        print(email)

    elif action == "Insert":
        index = int(data[1])
        char = data[2]
        email = email[:index] + char + email[index:]
        print(email)

    elif action == "Change":
        char = data[1]
        value = int(data[2])
        new_char = chr(ord(char) + value)
        if char in email:
            email = email.replace(char, new_char)
            print(email)
        else:
            command = input()
            continue

    elif action == "Validation":
        if len(email) < 6:
            print("Email must be at least 6 characters long!")
        not_valid = False
        for el in email:
            if not el.isalpha() and not el == "@":
                not_valid = True
        if not_valid:
            print("Email must consist only of letters, digits and @!")
        is_upper = False
        for el in email:
            if el.isupper():
                is_upper = True
        if not is_upper:
            print("Email must consist at least one uppercase letter!")
        is_lower = False
        for el in email:
            if el.islower():
                is_lower = True
        if not is_lower:
            print("Email must consist at least one lowercase letter!")
        is_digit = False
        for el in email:
            if el.isdigit():
                is_digit = True
        if not is_digit:
            print("Email must consist at least one digit!")
    else:
        command = input()
        continue

    command = input()
