command = input()

people = {}

while not command == "Results":
    data = command.split(":")
    action = data[0]

    if action == "Add":
        person_name = data[1]
        health = int(data[2])
        energy = int(data[3])
        if person_name not in people:
            people[person_name] = {"health": health, "energy": energy}
        else:
            people[person_name]["health"] += health

    elif action == "Attack":
        attacker_name = data[1]
        defender_name = data[2]
        damage = int(data[3])
        if attacker_name in people and defender_name in people:
            people[defender_name]["health"] -= damage
            people[attacker_name]["energy"] -= 1
            if people[defender_name]["health"] <= 0:
                people.pop(defender_name)
                print(f"{defender_name} was disqualified!")
            if people[attacker_name]["energy"] <= 0:
                people.pop(attacker_name)
                print(f"{attacker_name} was disqualified!")

    elif action == "Delete":
        user_name = data[1]
        if user_name == "All":
            people.clear()
        else:
            if user_name in people:
                people.pop(user_name)

    command = input()

count_of_people_left = len(people)

print(f"People count: {count_of_people_left}")

sorted_people = sorted(people.items(), key=lambda kvp: (-kvp[1]["health"], [0]))

for person_name, data in sorted_people:
    print(f"{person_name} - {data['health']} - {data['energy']}")
