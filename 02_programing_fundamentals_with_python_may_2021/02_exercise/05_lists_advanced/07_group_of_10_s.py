import math

numbers = input().split(", ")
numbers_as_int = [int(i) for i in numbers]

max_value = max(numbers_as_int)
count_boundary_groups = math.ceil(max_value / 10)

while numbers:
    for current_group in range(10, max_value + 10, 10):
        current_group_list = []
        for el in numbers_as_int:
            if current_group - 10 < el <= current_group:
                current_group_list.append(el)
                numbers.remove(str(el))
        print(f"Group of {current_group}'s: {current_group_list}")
