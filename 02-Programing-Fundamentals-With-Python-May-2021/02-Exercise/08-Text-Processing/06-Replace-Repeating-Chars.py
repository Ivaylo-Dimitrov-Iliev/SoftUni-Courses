string = input()

result = ""

curr_checked_index = 0

while curr_checked_index < len(string):
    curr_char = string[curr_checked_index]
    curr_sequence_length = 1
    for j in range(curr_checked_index + 1, len(string)):
        next_char = string[j]
        if curr_char == next_char:
            curr_sequence_length += 1
        else:
            break
    result += curr_char
    curr_checked_index += curr_sequence_length

print(result)
