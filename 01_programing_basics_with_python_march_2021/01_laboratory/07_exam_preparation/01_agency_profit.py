# input

company_name = input()
number_of_adult_tickets = int(input())
number_of_kid_tickets = int(input())
adult_price_per_ticket = float(input())
tax = float(input())

# variables

kids_price_per_ticket = adult_price_per_ticket * 0.3 + tax
adult_price_per_ticket += tax
total_income = number_of_adult_tickets * adult_price_per_ticket + number_of_kid_tickets * kids_price_per_ticket
company_profit = total_income * 0.20

print(f'The profit of your agency from {company_name} tickets is {company_profit:.2f} lv.')
