left_border_char = input()
right_border_char = input()
string = input()

result = 0

for i in range(len(string)):
    if ord(string[i]) in range(ord(left_border_char), ord(right_border_char)):
        result += int(ord(string[i]))

print(result)
