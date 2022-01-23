length = float(input())
width = float(input())

length_cm = length * 100
width_cm = width * 100

width_cm -= 100

number_of_desks_width = width_cm // 70
number_of_desks_length = length_cm // (40 + 80)

total_number_of_desks = number_of_desks_width * number_of_desks_length - 3

print(int(total_number_of_desks))
