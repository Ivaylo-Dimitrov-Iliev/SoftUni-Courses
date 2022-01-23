import re

pattern = r"\b[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+\b"

text = input()

valid_names = re.findall(pattern, text)

print(" ".join(valid_names))
