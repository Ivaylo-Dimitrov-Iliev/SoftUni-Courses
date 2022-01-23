# input

name = input()
password = input()

# loop

while True:
    new_password = input()
    if new_password == password:
        break

# output

print(f'Welcome {name}!')
