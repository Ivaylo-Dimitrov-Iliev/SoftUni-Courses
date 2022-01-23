rooms = input().split("|")

health = 100
coins = 0
room_counter = 0

for current_room in rooms:
    room_counter += 1
    current_room_data_list = current_room.split()
    kind = current_room_data_list[0]
    value = int(current_room_data_list[1])
    if kind == "potion":
        if health + value <= 100:
            health += value
            print(f"You healed for {value} hp.")
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {100 - health} hp.")
            health = 100
            print(f"Current health: {health} hp.")
    elif kind == "chest":
        coins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if not health <= 0:
            print(f"You slayed {kind}.")
        else:
            print(f"You died! Killed by {kind}.")
            print(f"Best room: {room_counter}")
            break

if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {coins}")
    print(f"Health: {health}")
