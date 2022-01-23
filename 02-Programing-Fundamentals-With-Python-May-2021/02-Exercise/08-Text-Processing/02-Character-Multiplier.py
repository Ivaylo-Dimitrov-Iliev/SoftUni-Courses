strings = input().split()
str_1 = strings[0]
str_2 = strings[1]

total_sum = 0
shorter_str_length = min(len(str_1), len(str_2))

for i in range(shorter_str_length):
    str_1_curr_char = str_1[i]
    str_2_curr_char = str_2[i]
    product = ord(str_1_curr_char) * ord(str_2_curr_char)
    total_sum += product

longer_str_length = max(len(str_1), len(str_2))

for i in range(shorter_str_length, longer_str_length):
    if len(str_1) > len(str_2):
        curr_char = str_1[i]
    else:
        curr_char = str_2[i]
    total_sum += ord(curr_char)

print(total_sum)
