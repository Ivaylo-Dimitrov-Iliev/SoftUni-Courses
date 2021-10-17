#input

from math import pi

figure_type = str(input())

#secondary input

if figure_type == "square":
    side_length = float(input())

elif figure_type == "rectangle":
    first_side_length = float(input())
    second_side_length = float(input())

elif figure_type == "circle":
    radius_length = float(input())

elif figure_type == "triangle":
    base_length = float(input())
    height_length = float(input())

#calculations

if figure_type == "square":
    square_area = side_length * side_length

elif figure_type == "rectangle":
    rectangle_area = first_side_length * second_side_length

elif figure_type == "circle":
    circle_area = pi * radius_length * radius_length

elif figure_type == "triangle":
    triangle_area = base_length * height_length / 2

#output

if figure_type == "square":
    print(f"{square_area:.3f}")

elif figure_type == "rectangle":
    print(f"{rectangle_area:.3f}")

elif figure_type == "circle":
    print(f"{circle_area:.3f}")

elif figure_type == "triangle":
    print(f"{triangle_area:.3f}")
