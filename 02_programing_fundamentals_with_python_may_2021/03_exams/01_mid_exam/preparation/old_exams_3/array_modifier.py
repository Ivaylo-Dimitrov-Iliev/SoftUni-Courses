array_of_integers = [int(el) for el in input().split()]

command = input()

while not command == "end":
    command_data_list = command.split()
    action = command_data_list[0]
    if action == "swap":
        index_1 = int(command_data_list[1])
        index_2 = int(command_data_list[2])
        array_of_integers[index_1], array_of_integers[index_2] = \
            array_of_integers[index_2], array_of_integers[index_1]
    elif action == "multiply":
        index_1 = int(command_data_list[1])
        index_2 = int(command_data_list[2])
        product = array_of_integers[index_1] * array_of_integers[index_2]
        array_of_integers[index_1] = product
    elif action == "decrease":
        array_of_integers = [el - 1 for el in array_of_integers]

    command = input()

array_of_integers = [str(el) for el in array_of_integers]

print(", ".join(array_of_integers))
