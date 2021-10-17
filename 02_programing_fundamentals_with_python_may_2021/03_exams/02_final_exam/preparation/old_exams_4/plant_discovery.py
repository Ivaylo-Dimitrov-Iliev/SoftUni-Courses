n = int(input())

plants_dict = {}

for _ in range(n):
    plant, rarity = input().split("<->")
    plants_dict[plant] = {"rarity": rarity, "rating": []}

command = input()

while not command == "Exhibition":
    data = command.split(":")
    action = data[0]
    if action == "Rate":
        plant, rating = data[1].split(" - ")
        if plant in plants_dict:
            plants_dict[plant]["rating"].append(int(rating))
        else:
            print("error")

    elif action == "Update":
        plant, new_rarity = data[1].split(" - ")
        if plant in plants_dict:
            plants_dict[plant]["rarity"] = new_rarity
        else:
            print("error")

    elif action == "Reset":
        plant = data[1]
        if plant in plants_dict:
            plants_dict[plant]["rating"].clear()
        else:
            print("error")

    command = input()

for plant, value in plants_dict.items():
    if not value["rating"]:
        plants_dict[plant]["rating"] = 0
    else:
        plants_dict[plant]["rating"] = sum(plants_dict[plant]["rating"]) / len(plants_dict[plant]["rating"])

sorted_plants = sorted(plants_dict, key=lambda kvp: (-kvp[1]["rarity"], -kvp[1]["rating"]))

print("Plants for the exhibition:")

for plant, value in sorted_plants:
    print(f"- {plant}; Rarity: {value['rarity']}; Rating: {value['rating']:.2f}")
