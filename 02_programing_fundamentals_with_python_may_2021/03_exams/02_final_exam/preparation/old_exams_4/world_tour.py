stops = input()

command = input()

while not command == "Travel":
    data = command.split(":")
    action = data[0]

    if action == "Add Stop":
        index = int(data[1])
        string = data[2]
        if index in range(len(stops)):
            left_half_stops = stops[:index]
            right_half_stops = stops[index:]
            stops = left_half_stops + string + right_half_stops

    elif action == "Remove Stop":
        start_index = int(data[1])
        end_index = int(data[2])
        if start_index in range(len(stops)) and end_index in range(len(stops)):
            substring = stops[start_index:end_index + 1]
            stops = stops.replace(substring, "")

    elif action == "Switch":
        old_string = data[1]
        new_string = data[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)

    print(stops)

    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
