#input

from math import floor

income = float(input())
average_mark = float(input())
minimal_wage = float(input())

#calculations

social_scholarship = floor(minimal_wage * 0.35)
excellence_scholarship = floor(average_mark * 25)


#output

if average_mark <= 4.5:
    print("You cannot get a scholarship!")
elif 5.5 > average_mark > 4.5 and income >= minimal_wage:
    print("You cannot get a scholarship!")
elif 5.5 > average_mark > 4.5 and income < minimal_wage:
    print(f"You get a Social scholarship {social_scholarship} BGN")
elif average_mark >= 5.5 and income >= minimal_wage:
    print(f"You get a scholarship for excellent results {excellence_scholarship} BGN")
elif average_mark >= 5.5 and income < minimal_wage and excellence_scholarship >= social_scholarship:
    print(f"You get a scholarship for excellent results {excellence_scholarship} BGN")
elif average_mark >= 5.5 and income < minimal_wage and excellence_scholarship < social_scholarship:
    print(f"You get a Social scholarship {social_scholarship} BGN")
