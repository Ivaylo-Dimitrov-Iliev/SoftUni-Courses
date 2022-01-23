string = input()

new_string = ""
temporary_string = ""
temporary_repeat_count = ""

for i in range(len(string)):
    if string[i].isalpha():
        curr_el = string[i]
        curr_el = curr_el.upper()
        temporary_string += curr_el
    elif string[i].isdigit():
        temporary_repeat_count += string[i]
        if i < (len(string) - 1) and string[i + 1].isdigit():
            continue
        new_string += temporary_string * int(temporary_repeat_count)
        temporary_string = ""
        temporary_repeat_count = ""
    else:
        temporary_string += string[i]

print(f"Unique symbols used: {len(set(new_string))}")
print(new_string)
