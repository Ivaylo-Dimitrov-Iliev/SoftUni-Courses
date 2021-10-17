import re

pattern = r"(?P<surr>.+)>(?P<nums>\d{3})(?P<sep>[|])(?P<low_c_l>[a-z]{3})(?P=sep)" + \
          r"(?P<upp_c_l>[A-Z]{3})(?P=sep)(?P<any_char>[^<>]+)<(?P=surr)"

count_of_passwords = int(input())

for _ in range(count_of_passwords):
    password = input()
    match = re.match(pattern, password)
    if not match:
        print("Try another password!")
    else:
        nums = match.group("nums")
        low_case_chars = match.group("low_c_l")
        upp_case_chars = match.group("upp_c_l")
        other_chars = match.group("any_char")
        encrypted_password = nums + low_case_chars + upp_case_chars + other_chars
        print(encrypted_password)

