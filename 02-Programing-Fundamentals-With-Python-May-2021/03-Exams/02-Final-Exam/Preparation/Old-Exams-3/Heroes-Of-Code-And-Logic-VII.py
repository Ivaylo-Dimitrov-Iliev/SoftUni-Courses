count_of_heroes = int(input())

heroes = {}

for _ in range(count_of_heroes):
    hero = input()
    hero_data = hero.split()
    hero_name = hero_data[0]
    hit_points = int(hero_data[1])
    mana_points = int(hero_data[2])
    heroes[hero_name] = {"hit_points": hit_points, "mana_points": mana_points}

command = input()

while not command == "End":
    data = command.split(" - ")
    action = data[0]
    hero_name = data[1]

    if action == "CastSpell":
        mana_power_needed = int(data[2])
        spell_name = data[3]
        if heroes[hero_name]["mana_points"] < mana_power_needed:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
        else:
            heroes[hero_name]["mana_points"] -= mana_power_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana_points']} MP!")

    elif action == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        heroes[hero_name]["hit_points"] -= damage
        if heroes[hero_name]["hit_points"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hit_points']} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif action == "Recharge":
        amount = int(data[2])
        amount_recovered = 200 - heroes[hero_name]["mana_points"]
        heroes[hero_name]["mana_points"] += amount
        if heroes[hero_name]["mana_points"] > 200:
            heroes[hero_name]["mana_points"] = 200
            print(f"{hero_name} recharged for {amount_recovered} MP!")
        else:
            print(f"{hero_name} recharged for {amount} MP!")

    elif action == "Heal":
        amount = int(data[2])
        amount_recovered = 100 - heroes[hero_name]["hit_points"]
        heroes[hero_name]["hit_points"] += amount
        if heroes[hero_name]["hit_points"] > 100:
            heroes[hero_name]["hit_points"] = 100
            print(f"{hero_name} healed for {amount_recovered} HP!")
        else:
            print(f"{hero_name} healed for {amount} HP!")

    command = input()

sorted_heroes = sorted(heroes.items(), key=lambda kvp: (-kvp[1]["hit_points"], kvp[0]))

for hero_name, data in sorted_heroes:
    print(hero_name)
    print(f"  HP: {data['hit_points']}")
    print(f"  MP: {data['mana_points']}")
