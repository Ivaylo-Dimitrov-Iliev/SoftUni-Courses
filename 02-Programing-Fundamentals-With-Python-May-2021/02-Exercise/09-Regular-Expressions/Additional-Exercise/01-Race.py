import re

participants_input = input().split(", ")

participants = {}

for participant in participants_input:
    participants[participant] = 0

pattern = r"[A-Za-z0-9]"

info = input()

while not info == "end of race":
    matched_chars = re.findall(pattern, info)
    participant_name = ""
    distance = 0
    for el in matched_chars:
        if el.isalpha():
            participant_name += el
        elif el.isnumeric():
            distance += int(el)
    if participant_name in participants:
        participants[participant_name] += distance

    info = input()

sorted_participants = sorted(participants.items(), key=lambda x: -x[1])

i = 0

for key, value in sorted_participants:
    i += 1
    suffix = ""
    if i == 1:
        suffix += "st"
    elif i == 2:
        suffix += "nd"
    elif i == 3:
        suffix += "rd"
    if i > 3:
        break
    print(f"{i}{suffix} place: {key}")
