working_day_events = input().split("|")

energy = 100
coins = 100

for current_event in working_day_events:
    current_event_data_list = current_event.split("-")
    event = current_event_data_list[0]
    value_of_event = int(current_event_data_list[1])
    if event == "rest":
        if energy + value_of_event <= 100:
            energy += value_of_event
            print(f"You gained {value_of_event} energy.")
        else:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy - 30 >= 0:
            coins += value_of_event
            energy -= 30
            print(f"You earned {value_of_event} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        coins -= value_of_event
        if not coins <= 0:
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            exit()

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
