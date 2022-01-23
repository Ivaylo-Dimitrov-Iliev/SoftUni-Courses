import re

pattern = r"(?P<url>(?P<sub_domain>w{3})\.(?P<domain>[A-Za-z0-9]+([\-A-Za-z0-9]+)*)(?P<domain_extension>(\.[a-z]+)+))"

text = input()

while text:
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match.group("url"))
    text = input()
