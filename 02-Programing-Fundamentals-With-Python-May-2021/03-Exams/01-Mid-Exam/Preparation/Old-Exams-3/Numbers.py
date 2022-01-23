integers = [int(x) for x in input().split()]

average_value = sum(integers) / len(integers)

list_of_top_5 = []

for el in integers:
    max_value = max(integers)
    if max_value > average_value and len(list_of_top_5) < 5:
        list_of_top_5.append(max_value)
        integers.remove(max_value)

if len(list_of_top_5) > 0:
    list_of_top_5 = [str(el) for el in list_of_top_5]
    print(" ".join(list_of_top_5))
else:
    print("No")
