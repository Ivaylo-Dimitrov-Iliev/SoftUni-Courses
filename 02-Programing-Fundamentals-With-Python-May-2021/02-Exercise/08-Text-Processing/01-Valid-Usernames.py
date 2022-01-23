usernames = input().split(", ")

list_of_valid_usernames = []

for current_name in usernames:
    if 3 <= len(current_name) <= 16:
        current_test_name = ""
        for el in current_name:
            if el.isalpha() or el.isdigit() or el == "-" or el == "_":
                current_test_name += el
        if current_test_name == current_name:
            list_of_valid_usernames.append(current_name)

[print(current_name) for current_name in list_of_valid_usernames]
