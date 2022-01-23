import sys


def exchange_indexes(list, index):
    list_of_integers = []
    exchanged_list = []
    for digit in list:
        list_of_integers.append(int(digit))
    if not 0 <= index < len(list):
        print("Invalid index")
        exchanged_list = list_of_integers
    else:
        list_first_part = list_of_integers[:int(data[1]) + 1]
        list_second_part = list_of_integers[int(data[1]) + 1:]
        exchanged_list = list_second_part + list_first_part
    return exchanged_list


def max_even_odd(list, command):
    data = command.split()
    list_of_integers = []
    for current_digit in list:
        list_of_integers.append(int(current_digit))
    max_even_value = -sys.maxsize
    max_odd_value = -sys.maxsize
    max_even_position = 0
    max_odd_position = 0
    for current_digit in range(len(list_of_integers)):
        if list_of_integers[current_digit] % 2 == 0 and list_of_integers[current_digit] >= max_even_value:
            max_even_value = list_of_integers[current_digit]
            max_even_position = current_digit
        elif list_of_integers[current_digit] % 2 == 1 and list_of_integers[current_digit] >= max_odd_value:
            max_odd_value = list_of_integers[current_digit]
            max_odd_position = current_digit
    if not max_even_value == -sys.maxsize and data[1] == "even":
        return max_even_position
    elif not max_odd_value == -sys.maxsize and data[1] == "odd":
        return max_odd_position
    else:
        return "No matches"


def min_even_odd(list, command):
    data = command.split()
    list_of_integers = []
    for current_digit in list:
        list_of_integers.append(int(current_digit))
    min_even_value = sys.maxsize
    min_odd_value = sys.maxsize
    min_even_position = 0
    min_odd_position = 0
    for current_digit in range(len(list_of_integers)):
        if list_of_integers[current_digit] % 2 == 0 and list_of_integers[current_digit] <= min_even_value:
            min_even_value = list_of_integers[current_digit]
            min_even_position = current_digit
        elif list_of_integers[current_digit] % 2 == 1 and list_of_integers[current_digit] <= min_odd_value:
            min_odd_value = list_of_integers[current_digit]
            min_odd_position = current_digit
    if not min_even_value == sys.maxsize and data[1] == "even":
        return min_even_position
    elif not min_odd_value == sys.maxsize and data[1] == "odd":
        return min_odd_position
    else:
        return "No matches"


def first_count_even_odd(list, command):
    data = command.split()
    even_counter = 0
    odd_counter = 0
    list_of_integers = []
    list_of_evens = []
    list_of_odds = []
    if int(data[1]) > len(list):
        return "Invalid count"
    for current_digit in list:
        list_of_integers.append(int(current_digit))
    for current_digit in list_of_integers:
        if current_digit % 2 == 0:
            if int(data[1]) == even_counter:
                break
            else:
                list_of_evens.append(current_digit)
                even_counter += 1
        elif current_digit % 2 == 1:
            if int(data[1]) == odd_counter:
                break
            else:
                list_of_odds.append(current_digit)
                odd_counter += 1
    if data[2] == "even":
        return list_of_evens
    elif data[2] == "odd":
        return list_of_odds


def last_count_even_odd(list, command):
    data = command.split()
    even_counter = 0
    odd_counter = 0
    list_of_integers = []
    list_of_evens = []
    list_of_odds = []
    if int(data[1]) > len(list):
        return "Invalid count"
    for current_digit in list:
        list_of_integers.append(int(current_digit))
    for current_digit in list_of_integers[::-1]:
        if current_digit % 2 == 0:
            if int(data[1]) == even_counter:
                break
            else:
                list_of_evens.append(current_digit)
                even_counter += 1
        elif current_digit % 2 == 1:
            if int(data[1]) == odd_counter:
                break
            else:
                list_of_odds.append(current_digit)
                odd_counter += 1
    if data[2] == "even":
        reversed_list_of_evens = list_of_evens[::-1]
        return reversed_list_of_evens
    elif data[2] == "odd":
        reversed_list_of_odds = list_of_odds[::-1]
        return reversed_list_of_odds


def stringify_list(list, delimiter: str):
    parsed_list = []
    for current_number in list:
        parsed_list.append(str(current_number))
    return delimiter.join(parsed_list)


input_list = input().split()
input_command = input()

while not input_command == "end":
    data = input_command.split()
    if data[0] == "exchange":
        input_index = int(data[1])
        input_list = exchange_indexes(input_list, input_index)
    elif data[0] == "max":
        print(max_even_odd(input_list, input_command))
    elif data[0] == "min":
        print(min_even_odd(input_list, input_command))
    elif data[0] == "first":
        print(first_count_even_odd(input_list, input_command))
    elif data[0] == "last":
        print(last_count_even_odd(input_list, input_command))
    input_command = input()

print(f"[{stringify_list(input_list, ', ')}]")
