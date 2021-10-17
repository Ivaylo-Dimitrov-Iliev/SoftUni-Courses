string = input()

result_text = ""
bomb_range = 0
curr_check_index = 0

while curr_check_index < len(string):
    curr_char = string[curr_check_index]
    if not curr_char == ">":
        result_text += curr_char
    else:
        result_text += curr_char
        bomb_range += int(string[curr_check_index + 1])
        while bomb_range > 0:
            curr_check_index += 1
            if curr_check_index >= len(string):
                break
            curr_char = string[curr_check_index]
            if curr_char == ">":
                result_text += curr_char
                bomb_range += int(string[curr_check_index + 1])
            else:
                bomb_range -= 1
    curr_check_index += 1

print(result_text)
