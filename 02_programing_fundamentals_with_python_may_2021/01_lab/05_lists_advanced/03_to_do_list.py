list_of_notes = [0] * 10

command = input()

while not command == "End":
    importance, activity = command.split("-")
    current_index = int(importance) - 1
    list_of_notes[current_index] = activity

    command = input()

print([el for el in list_of_notes if not el == 0])