#input

import math
number_of_campaign_days = int(input())
number_of_confectioners = int(input())
number_of_cakes_per_day_per_confectioner = int(input())
number_of_waffles_per_day_per_confectioner = int(input())
number_of_pancakes_per_day_per_confectioner = int(input())

#calculations

total_number_of_cakes = number_of_campaign_days * number_of_confectioners * number_of_cakes_per_day_per_confectioner
total_income_from_cakes_lv = total_number_of_cakes * 45

total_number_of_waffles = number_of_campaign_days * number_of_confectioners * number_of_waffles_per_day_per_confectioner
total_income_from_waffles_lv = total_number_of_waffles * 5.8

total_number_of_pancakes = number_of_campaign_days * number_of_confectioners * number_of_pancakes_per_day_per_confectioner
total_income_from_pancakes_lv = total_number_of_pancakes * 3.2

total_income = total_income_from_cakes_lv + total_income_from_waffles_lv + total_income_from_pancakes_lv

charity_income = total_income - total_income * 0.125

#output

print(round(charity_income, 2))
