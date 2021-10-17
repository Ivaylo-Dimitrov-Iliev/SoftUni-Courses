n = int(input())

parking_dict = {}

for i in range(0, n):
    command = input()
    data_list = command.split()
    action = data_list[0]
    name = data_list[1]
    if action == "register":
        number = data_list[2]
        if name not in parking_dict:
            parking_dict[name] = number
            print(f"{name} registered {number} successfully")
        else:
            print(f"ERROR: already registered with plate number {number}")
    elif action == "unregister":
        if name not in parking_dict:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            parking_dict.pop(name)

for name, number in parking_dict.items():
    print(f"{name} => {number}")