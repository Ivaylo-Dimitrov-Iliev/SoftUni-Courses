number_of_wagons = int(input())

list_of_wagons = [0] * number_of_wagons

command = input()

while not command == "End":
    command_data_list = command.split()
    if command_data_list[0] == "add":
        list_of_wagons[-1] += int(command_data_list[1])
    elif command_data_list[0] == "insert":
        index = int(command_data_list[1])
        number_passengers = int(command_data_list[2])
        list_of_wagons[index] += number_passengers
    elif command_data_list[0] == "leave":
        index = int(command_data_list[1])
        number_passengers = int(command_data_list[2])
        list_of_wagons[index] -= number_passengers

    command = input()

print(list_of_wagons)
