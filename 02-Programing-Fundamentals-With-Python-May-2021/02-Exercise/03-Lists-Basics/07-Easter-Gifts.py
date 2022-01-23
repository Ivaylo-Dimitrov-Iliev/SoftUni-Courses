list_of_gifts = input().split()
command = input()

while not command == "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        for i, el in enumerate(list_of_gifts):
            if el == command[1]:
                list_of_gifts[i] = "None"
    elif command[0] == "Required":
        if int(command[2]) in range(len(list_of_gifts)):
            list_of_gifts.pop(int(command[2]))
            list_of_gifts.insert(int(command[2]), command[1])
    elif command[0] == "JustInCase":
        list_of_gifts.pop()
        list_of_gifts.append(command[1])

    command = input()

for i in range(len(list_of_gifts)):
    if not i == len(list_of_gifts) - 1 and not list_of_gifts[i] == "None":
        print(list_of_gifts[i], end=" ")
    elif i == len(list_of_gifts) - 1 and not list_of_gifts[i] == "None":
        print(list_of_gifts[i])
