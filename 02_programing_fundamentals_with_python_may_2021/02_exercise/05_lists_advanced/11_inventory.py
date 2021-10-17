items = input().split(", ")

command = input()

while not command == "Craft!":
    command_data_list = command.split(" - ")
    action = command_data_list[0]
    item = command_data_list[1]
    if action == "Collect":
        if item not in items:
            items.append(item)
    elif action == "Drop":
        if item in items:
            items.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in items:
            items.insert(items.index(old_item) + 1, new_item)
    elif action == "Renew":
        if item in items:
            items += [items.pop(items.index(item))]
    command = input()

print(*items, sep=", ")
