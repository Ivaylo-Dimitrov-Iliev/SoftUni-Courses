count_of_numbers = int(input())

for num in range(1, count_of_numbers + 1):
    nums_as_string = str(num)
    result = 0
    for symbol in nums_as_string:
        result += int(symbol)
    if result == 5 or result == 7 or result == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")