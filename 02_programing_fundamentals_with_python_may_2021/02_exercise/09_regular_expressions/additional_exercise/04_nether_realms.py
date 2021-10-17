import re

pattern = r"((?P<name>[^\s\,]+)(?P<num>[\+|\-]?[0-9]+[\.0-9]?)*)"

demons = input()

valid_demons = re.finditer(pattern, demons)
demons_dictionary = {}

for demon in valid_demons:
    name = demon.group("name")
    number = demon.group("num")
    health = 0
    damage = 0
    i = 0
    print(number)

# Variant 2
#     demons_dictionary[name] = {"health": health, "damage": damage}
#
# sorted_demons = sorted(demons_dictionary.items(), key=lambda x: x[0])
#
# for key, value in sorted_demons:
#     print(f"{key} - {value['health']} health, {value['damage']:.2f} damage")
