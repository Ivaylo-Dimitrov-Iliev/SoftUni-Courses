def perfect_number(number):
    half_number = number // 2
    divisors = []
    for current_divisor in range(1, half_number + 1):
        if number % current_divisor == 0:
            divisors.append(current_divisor)
    sum_of_divisors = sum(divisors)
    if sum_of_divisors == number:
        message = "We have a perfect number!"
    else:
        message = "It's not so perfect."
    return message


number_input = int(input())

print(perfect_number(number_input))
