import re

text = input()

pattern = r"(^|(?<=\s))(?P<email>(?P<user>[a-z0-9]+[\.\_\-a-z0-9]*)@(?P<host>[a-z0-9]+[\-a-z]*\.[a-z]+[\.a-z]*))\b"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group("email"))
