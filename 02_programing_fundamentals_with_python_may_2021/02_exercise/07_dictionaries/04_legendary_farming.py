key_resources = {"shards": 0, "fragments": 0, "motes": 0}
junk_resources = {}
legendary_item = ""

while legendary_item == "":
    resources = input().split()
    for i in range(0, len(resources), 2):
        if not legendary_item == "":
            break
        resource = resources[i + 1].lower()
        quantity = int(resources[i])
        if resource == "shards" or resource == "fragments" or resource == "motes":
            key_resources[resource] += quantity
            for resource, quantity in key_resources.items():
                if resource == "shards" and quantity >= 250:
                    legendary_item = "Shadowmourne"
                    key_resources[resource] -= 250
                    break
                elif resource == "fragments" and quantity >= 250:
                    legendary_item = "Valanyr"
                    key_resources[resource] -= 250
                    break
                elif resource == "motes" and quantity >= 250:
                    legendary_item = "Dragonwrath"
                    key_resources[resource] -= 250
                    break
        else:
            if resource not in junk_resources:
                junk_resources[resource] = 0
            junk_resources[resource] += quantity

print(f"{legendary_item} obtained!")

sorted_key_resources = (sorted(key_resources.items(), key=lambda el: (-el[1], el[0])))

for resource, quantity in sorted_key_resources:
    print(f"{resource}: {quantity}")

sorted_junk_resources = (sorted(junk_resources.items(), key=lambda x: x[0]))

for resource, quantity in sorted_junk_resources:
    print(f"{resource}: {quantity}")