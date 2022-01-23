strings = input().split()

result = [el * len(el) for el in strings]

print(f"{''.join(result)}")