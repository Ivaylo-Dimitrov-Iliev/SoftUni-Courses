x = float(input())
y = float(input())
h = float(input())

walls_area = (2 * (x * x) - (2 * 1.2)) + 2 * (x * y - (1.5 * 1.5))
roof_area = 2 * (x * y) + (x * h)

green_paint_expense = walls_area / 3.4
red_paint_expense = roof_area / 4.3

print(f'{green_paint_expense:.2f}')
print(f'{red_paint_expense:.2f}')
