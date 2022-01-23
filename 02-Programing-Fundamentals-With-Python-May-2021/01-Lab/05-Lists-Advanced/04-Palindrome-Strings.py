list_of_words = input().split()
palindrome_word = input()

print([el for el in list_of_words if el == el[::-1]])

print(f"Found palindrome {list_of_words.count(palindrome_word)} times")
