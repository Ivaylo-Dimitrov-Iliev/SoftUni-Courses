number = int(input())

for i in range(0, number):
    for j in range(0, number):
        for k in range(0, number):
            print(f"{chr(i + 97)}{chr(j + 97)}{chr(k + 97)}")
