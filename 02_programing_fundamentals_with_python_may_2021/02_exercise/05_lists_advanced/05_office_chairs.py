count_of_rooms = int(input())

free_chairs = 0

for current_room in range(1, count_of_rooms +1):
    command = input().split()
    chairs, visitors = command
    if len(chairs) < int(visitors):
        print(f"{int(visitors) - len(chairs)} more chairs needed in room {current_room}")
        free_chairs -= (int(visitors) - len(chairs))
    else:
        free_chairs += len(chairs) - int(visitors)

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
