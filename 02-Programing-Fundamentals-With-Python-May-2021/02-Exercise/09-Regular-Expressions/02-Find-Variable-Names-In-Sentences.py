import re

text = input()

pattern = r"\b_(?P<variable_name>[A-Za-z0-9]+)\b"

matches = re.finditer(pattern, text)

valid_variables =[]

for match in matches:
    valid_variables.append(match.group("variable_name"))

print(",".join(valid_variables))

#print(",".join([match.group("variable_name") for match in re.finditer(pattern, text)]))
