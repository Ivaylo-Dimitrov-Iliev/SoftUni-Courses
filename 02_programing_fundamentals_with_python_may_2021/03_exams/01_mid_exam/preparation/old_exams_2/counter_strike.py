energy = int(input())

command = input()

count_of_won_battles = 0

while not command == "End of battle":
    distance = int(command)
    if energy - distance < 0:
        print(f"Not enough energy! Game ends with {count_of_won_battles} won battles and {energy} energy")
        exit()
    else:
        energy -= distance
    count_of_won_battles += 1
    if count_of_won_battles % 3 == 0:
        energy += count_of_won_battles

    command = input()

print(f"Won battles: {count_of_won_battles}. Energy left: {energy}")
