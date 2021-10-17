targets = [int(el) for el in input().split()]

command = input()

while not command == "End":
    command_data_list = command.split()
    action = command_data_list[0]
    index = int(command_data_list[1])
    if action == "Shoot":
        power = int(command_data_list[2])
        if 0 <= index <= len(targets) - 1:
            targets[index] -= power
            if targets[index] <= 0:
                del targets[index]
    elif action == "Add":
        value = int(command_data_list[2])
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        radius = int(command_data_list[2])
        if 0 <= radius <= (len(targets) - 1) // 2 and index - radius >= 0:
            del targets[index - radius:index + radius + 1]
        else:
            print("Strike missed!")
    command = input()

print(*targets, sep="|")
