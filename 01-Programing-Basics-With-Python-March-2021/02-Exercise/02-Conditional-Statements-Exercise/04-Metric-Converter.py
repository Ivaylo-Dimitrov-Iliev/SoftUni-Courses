#input

number = float(input())
measurement_unit_in = str(input())
measurement_unit_out = str(input())

#output

if measurement_unit_in == "m" and measurement_unit_out == "cm":
    print(f"{number * 100:.3f}")
elif measurement_unit_in == "m" and measurement_unit_out == "mm":
    print(f"{number * 1000:.3f}")
elif measurement_unit_in == "cm" and measurement_unit_out == "m":
    print(f"{number * 0.01:.3f}")
elif measurement_unit_in == "cm" and measurement_unit_out == "mm":
    print(f"{number * 10:.3f}")
elif measurement_unit_in == "mm" and measurement_unit_out == "cm":
    print(f"{number * 0.1:.3f}")
elif measurement_unit_in == "mm" and measurement_unit_out == "m":
    print(f"{number * 0.001:.3f}")
