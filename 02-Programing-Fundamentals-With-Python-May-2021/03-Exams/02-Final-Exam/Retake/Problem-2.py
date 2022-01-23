import  re

pattern = r"([@|#]+(?P<color>[a-z]{3,})[@|#]+)([^\w])*(?P<surr>/+)(?P<amount>\d+)(?P<surr_2>/+)"

eggs = input()

valid_eggs = re.finditer(pattern, eggs)

for egg in valid_eggs:
    color = egg.group("color")
    amount = egg.group("amount")
    print(f"You found {amount} {color} eggs!")