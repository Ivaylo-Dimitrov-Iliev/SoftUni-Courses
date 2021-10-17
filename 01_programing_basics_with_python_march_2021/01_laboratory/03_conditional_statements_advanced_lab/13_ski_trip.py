# input

stay_days = int(input())
chamber_type = input()
evaluation = input()

# variable

chamber_cost = 0

# statements

if chamber_type == 'room for one person':
    chamber_cost = 18.00

elif chamber_type == 'apartment':
    chamber_cost = 25.00
    if stay_days < 10:
        chamber_cost *= 0.70
    elif 10 <= stay_days <= 15:
        chamber_cost *= 0.65
    elif stay_days > 15:
        chamber_cost *= 0.50

elif chamber_type == 'president apartment':
    chamber_cost = 35.00
    if stay_days < 10:
        chamber_cost *= 0.90
    elif 10 <= stay_days <= 15:
        chamber_cost *= 0.85
    elif stay_days > 15:
        chamber_cost *= 0.80

# variable 2

final_cost = (stay_days - 1) * chamber_cost

# second discount statements

if evaluation == 'positive':
    final_cost *= 1.25
elif evaluation == 'negative':
    final_cost *= 0.90

print(f'{final_cost:.2f}')
