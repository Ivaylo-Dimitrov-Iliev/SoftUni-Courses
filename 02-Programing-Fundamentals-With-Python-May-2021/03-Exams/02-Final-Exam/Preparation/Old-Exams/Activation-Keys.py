activation_key = input()
command = input()

while not command == "Generate":

    if "Contains" in command:
        data = command.split(">>>")
        substring = data[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif "Flip" in command:
        data = command.split(">>>")
        action, case, start_index, end_index = data
        if case == "Upper":
            characters_for_flip = activation_key[int(start_index):int(end_index)]
            flipped_characters = activation_key[int(start_index):int(end_index)].upper()
            activation_key = activation_key.replace(characters_for_flip, flipped_characters)
        else:
            characters_for_flip = activation_key[int(start_index):int(end_index)]
            flipped_characters = activation_key[int(start_index):int(end_index)].lower()
            activation_key = activation_key.replace(characters_for_flip, flipped_characters)
        print(activation_key)

    elif "Slice" in command:
        data = command.split(">>>")
        action, start_index, end_index = data
        removed_slice = activation_key[int(start_index):int(end_index)]
        activation_key = activation_key.replace(removed_slice, "")
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")
