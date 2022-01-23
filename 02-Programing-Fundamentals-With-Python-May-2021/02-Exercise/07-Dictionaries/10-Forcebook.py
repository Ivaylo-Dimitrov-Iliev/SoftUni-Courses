command = input()

force_book = {}

while not command == "Lumpawaroo":
    if "|" in command:
        data = command.split(" | ")
        side, user = data
        if side not in force_book and user not in force_book:
            force_book[side] = [user]
        elif user not in force_book:
            force_book[side].append(user)
        elif user in force_book:
            continue
    elif "->" in command:
        data = command.split(" -> ")
        user, side = data
        if user in force_book:
            force_book.pop(user)
            force_book[side].append(user)
        elif user not in force_book:
            force_book[side].append(user)
        elif side not in force_book and user not in force_book:
            force_book[side] = [user]
        print(f"{user} joins the {side} side!")

    command = input()
#
# sorted_force_book = sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0]))
print(force_book)
