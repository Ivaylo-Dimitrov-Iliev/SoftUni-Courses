def odd_even_sum(number):
    sum_of_even_digits = 0
    sum_of_odd_digits = 0
    for current_digit in number:
        current_digit = int(current_digit)
        if current_digit % 2 == 0:
            sum_of_even_digits += current_digit
        elif current_digit % 2 == 1:
            sum_of_odd_digits += current_digit
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


input_number = input()

print(odd_even_sum(input_number))
