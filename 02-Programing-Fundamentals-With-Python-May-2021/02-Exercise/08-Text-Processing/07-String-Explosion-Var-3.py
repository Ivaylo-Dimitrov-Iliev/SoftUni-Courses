string = [x for x in input()]

power = 0

for i in range(len(string)):
    if string[i] == ">":
        power += int(string[i + 1])
    else:
        if power > 0:
            string[i] = " "
            power -= 1

new_string = [y for y in string if not y == " "]
print("".join(new_string))
