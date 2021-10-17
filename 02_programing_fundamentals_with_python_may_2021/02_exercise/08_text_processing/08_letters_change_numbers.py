sequence = input().split()

total_sum = 0

for el in sequence:
    first_letter = el[0]
    last_letter = el[-1]
    number = int(el[1:-1])
    if first_letter.isupper():
        resulted_number = number / (ord(first_letter) - 64)
    else:
        resulted_number = number * (ord(first_letter) - 96)
    if last_letter.isupper():
        final_product = resulted_number - (ord(last_letter) - 64)
    else:
        final_product = resulted_number + (ord(last_letter) - 96)

    total_sum += final_product

print(f"{total_sum:.2f}")
