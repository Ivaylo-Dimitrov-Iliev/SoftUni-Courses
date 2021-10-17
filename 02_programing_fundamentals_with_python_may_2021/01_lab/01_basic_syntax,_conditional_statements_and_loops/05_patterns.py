# input

number = int(input())

# loop

for row in range(1, number + 1):
    for column in range(0, row):
        print("*", end="")
    print()
for row in range(number -1, 0, -1):
    for column in range(0, row):
        print("*", end="")
    print()
