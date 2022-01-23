substring_to_remove = input()
string = input()

while substring_to_remove in string:
    string = string.replace(substring_to_remove, "")

print(string)
