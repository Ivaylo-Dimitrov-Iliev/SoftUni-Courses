initial_list = input().split("!")

command = input()

while not command == "Go Shopping!":
    command_data_list = command.split()
    category = command_data_list[0]
    item = command_data_list[1]
    if category == "Urgent" and item not in initial_list:
        initial_list.insert(0, item)
    elif category == "Unnecessary" and item in initial_list:
        initial_list.remove(item)
    elif category == "Correct" and item in initial_list:
        new_item = command_data_list[2]
        initial_list[initial_list.index(item)] = new_item
    elif category == "Rearrange" and item in initial_list:
        initial_list += [initial_list.pop(initial_list.index(item))]

    command = input()

print(", ".join(initial_list))
