def is_password_length_valid(password):
    if 6 <= len(password) <= 10:
        return True
    return False


def is_password_alphanumeric(password):
    is_alphanum = True
    for character in password:
        if not (character.isalpha() or character.isnumeric()):
            is_alphanum = False
            break
    return is_alphanum


def is_password_at_least_two_digits(password):
    digits_count = 0
    for current_symbol in password:
        if current_symbol.isdigit():
            digits_count += 1
    if digits_count >= 2:
        return True
    else:
        return False


def password_validator(password):
    is_password_valid = True
    if not is_password_length_valid(password):
        is_password_valid = False
        print("Password must be between 6 and 10 characters")
    if not is_password_alphanumeric(password):
        is_password_valid = False
        print("Password must consist only of letters and digits")
    if not is_password_at_least_two_digits(password):
        is_password_valid = False
        print("Password must have at least 2 digits")
    if is_password_valid:
        print("Password is valid")


password_input = input()

password_validator(password_input)
