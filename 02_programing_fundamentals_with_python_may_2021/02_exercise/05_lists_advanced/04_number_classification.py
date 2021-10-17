numbers = [int(i) for i in input().split(", ")]

positives = [str(num) for num in numbers if num >= 0]

negatives = [str(num) for num in numbers if num < 0]

even = [str(num) for num in numbers if num % 2 == 0]

odd = [str(num) for num in numbers if not num % 2 == 0]

print(f"Positive: {', '.join(positives)}")

print(f"Negative: {', '.join(negatives)}")

print(f"Even: {', '.join(even)}")

print(f"Odd: {', '.join(odd)}")
