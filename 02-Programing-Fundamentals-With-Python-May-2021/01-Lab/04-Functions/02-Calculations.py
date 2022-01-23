def calculation(a, b, operator):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


input_operator = input()
num1 = int(input())
num2 = int(input())

print(calculation(num1, num2, input_operator))
