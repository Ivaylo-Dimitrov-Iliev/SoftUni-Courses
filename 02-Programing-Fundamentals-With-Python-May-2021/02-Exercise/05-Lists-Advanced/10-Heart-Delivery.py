houses = [int(el) for el in input().split("@")]

command = input()
current_index = 0

while not command == "Love!":
    command_data_list = command.split()
    jump_index = int(command_data_list[1])
    current_index += jump_index
    if current_index > len(houses) - 1:
        current_index = 0
    if houses[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        houses[current_index] -= 2
        if houses[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")

    command = input()

print(f"Cupid's last position was {current_index}.")

valentine_houses = ([el for el in houses if el == 0])

if len(houses) == len(valentine_houses):
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {len(houses) - len(valentine_houses)} places.")
