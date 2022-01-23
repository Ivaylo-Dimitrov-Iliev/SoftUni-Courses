import re

n = int(input())

attacked_planets = 0
attacked_planets_list = []
destroyed_planets = 0
destroyed_planets_list = []

for _ in range(n):
    message = input()
    message_low = message.lower()
    s_counter = message_low.count("s")
    t_counter = message_low.count("t")
    a_counter = message_low.count("a")
    r_counter = message_low.count("r")
    total_counter = s_counter + t_counter + a_counter + r_counter
    decrypted_message = ""
    for el in message:
        el = chr(int(ord(el)) - int(total_counter))
        decrypted_message += el

    pattern = r"[^\@\!\:\>\-]*@(?P<name>[A-Za-z]+)[^\@\!\:\>\-]*\:(?P<population>\d+)[^\@\!\:\>\-]*\!(?P<attack_type>A|D)\![^\@\!\:\>\-]*->(?P<soldier_count>\d+)"

    valid_message = re.match(pattern, decrypted_message)

    if valid_message:
        type_of_attack = valid_message.group("attack_type")
        planet_name = valid_message.group("name")

        if type_of_attack == "A":
            attacked_planets += 1
            attacked_planets_list.append(planet_name)

        elif type_of_attack == "D":
            destroyed_planets += 1
            destroyed_planets_list.append(planet_name)

attacked_planets_list.sort()
destroyed_planets_list.sort()

print(f"Attacked planets: {attacked_planets}")
[print(f"-> {''.join(planet)}") for planet in attacked_planets_list]

print(f"Destroyed planets: {destroyed_planets}")
[print(f"-> {''.join(planet)}") for planet in destroyed_planets_list]