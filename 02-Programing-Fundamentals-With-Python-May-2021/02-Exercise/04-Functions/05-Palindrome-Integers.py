def palindromes(list_of_numbers):
    for current_element in list_of_integers:
        reversed_element = current_element[::-1]
        if reversed_element == current_element:
            result = "True"
        else:
            result = "False"
        print(result)


list_of_integers = input().split(", ")

palindromes(list_of_integers)
