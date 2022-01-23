sub_strings = input().split(", ")
list_of_words = input().split(", ")

print([current_sub for current_sub in sub_strings if current_sub in str(list_of_words)])
