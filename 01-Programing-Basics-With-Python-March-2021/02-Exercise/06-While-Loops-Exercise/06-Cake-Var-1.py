# input

cake_length = int(input())
cake_width = int(input())
command = input()

# calculations

cake_pieces = cake_length * cake_width

# loop

while command != 'STOP':
    taken_pieces = int(command)
    cake_pieces -= taken_pieces
    if cake_pieces < 0:
        print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')
        break
    command = input()
else:
    print(f'{cake_pieces} pieces are left.')
