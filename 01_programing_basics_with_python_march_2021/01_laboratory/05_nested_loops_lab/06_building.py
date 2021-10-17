# input

count_floors = int(input())
rooms_at_floor = int(input())

# loop

for floor in range(count_floors, 0, -1):
    for room in range(0, rooms_at_floor):
        if floor == count_floors:
            print(f'L{floor}{room}', end=' ')
        elif floor % 2 == 1:
            print(f'A{floor}{room}', end=' ')
        elif floor % 2 == 0:
            print(f'O{floor}{room}', end=' ')
    print()
