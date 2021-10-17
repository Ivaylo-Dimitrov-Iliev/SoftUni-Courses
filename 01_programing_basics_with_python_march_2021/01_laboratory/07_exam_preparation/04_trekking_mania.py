# input

number_of_climbers_groups = int(input())


# variables

total_climbers = 0
musala_climbers = 0
mont_blanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

# loop

for groups in range(1, number_of_climbers_groups + 1):
    count_of_climbers = int(input())
    if count_of_climbers <= 5:
        musala_climbers += count_of_climbers
    elif 5 < count_of_climbers <= 12:
        mont_blanc_climbers += count_of_climbers
    elif 12 < count_of_climbers <= 25:
        kilimanjaro_climbers += count_of_climbers
    elif 25 < count_of_climbers <= 40:
        k2_climbers += count_of_climbers
    elif count_of_climbers >= 41:
        everest_climbers += count_of_climbers
    total_climbers += count_of_climbers

# percentage calculations

percentage_musala_climbers = musala_climbers / total_climbers * 100
percentage_mont_blanc_climbers = mont_blanc_climbers / total_climbers * 100
percentage_kilimanjaro_climbers = kilimanjaro_climbers / total_climbers * 100
percentage_k2_climbers = k2_climbers / total_climbers * 100
percentage_everest_climbers = everest_climbers / total_climbers * 100

# output

print(f'{percentage_musala_climbers:.2f}%')
print(f'{percentage_mont_blanc_climbers:.2f}%')
print(f'{percentage_kilimanjaro_climbers:.2f}%')
print(f'{percentage_k2_climbers:.2f}%')
print(f'{percentage_everest_climbers:.2f}%')
