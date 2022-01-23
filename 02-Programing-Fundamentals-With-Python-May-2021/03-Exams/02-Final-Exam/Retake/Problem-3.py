command = input()

distributors = {}
clients = {}
total_income = 0

while not command == "End":
    action, name, money = command.split()
    if action == "Deliver":
        if name not in distributors:
            distributors[name] = float(money)
        else:
            distributors[name] += float(money)

    elif action == "Return":
        if name not in distributors:
            command = input()
            continue
        if distributors[name] < float(money):
            command = input()
            continue
        else:
            distributors[name] -= float(money)
            if distributors[name] == 0:
                distributors.pop(name)

    elif action == "Sell":
        if name not in clients:
            clients[name] = float(money)
            total_income += float(money)
        else:
            clients[name] += float(money)
            total_income += float(money)

    command = input()

sorted_clients = sorted(clients.items(), key=lambda x: x[0])

for name, money in sorted_clients:
    print(f"{name}: {money:.2f}")
print("-----------")

sorted_distributors = sorted(distributors.items(), key=lambda x: x[0])

for name, money in sorted_distributors:
    print(f"{name}: {money:.2f}")
print("-----------")
print(f"Total Income: {total_income:.2f}")
