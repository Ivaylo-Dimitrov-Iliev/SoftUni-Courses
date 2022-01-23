def factorial_division(a, b):
    fac_a = a
    fac_b = b
    while a > 1:
        fac_a *= a - 1
        a -= 1
    while b > 1:
        fac_b *= b - 1
        b -= 1
    result = fac_a / fac_b
    return result


num_1 = int(input())
num_2 = int(input())

print(f"{factorial_division(num_1, num_2):.2f}")
