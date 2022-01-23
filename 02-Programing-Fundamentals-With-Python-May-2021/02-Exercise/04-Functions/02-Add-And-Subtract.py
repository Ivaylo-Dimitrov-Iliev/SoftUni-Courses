def sum_numbers(a, b):
    return a + b


def subtract(sum_of_numbers, c):
    return sum_of_numbers - c


def add_and_subtract(a, b, c):
    sum_1 = sum_numbers(a, b)
    result = sum_1 - c
    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(add_and_subtract(num_1, num_2, num_3))
