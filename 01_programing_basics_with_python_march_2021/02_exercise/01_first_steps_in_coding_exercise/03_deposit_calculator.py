#input

deposit_amount = int(input())
deposit_term = int(input())
annual_interest_rate = float(input())

#calculation

percent = annual_interest_rate * 0.01
amount = deposit_amount + deposit_term * ((deposit_amount * percent) /12)

#output

print(amount)
