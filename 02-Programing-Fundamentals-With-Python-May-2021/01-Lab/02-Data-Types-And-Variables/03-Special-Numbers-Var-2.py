count_of_numbers = int(input())

for num in range(1, count_of_numbers + 1):
    result = 0
    digits = num
    while digits > 0:
        result += digits % 10
        digits = int(digits / 10)
    if result == 5 or result == 7 or result == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")