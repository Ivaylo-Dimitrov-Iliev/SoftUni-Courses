price_vegetables = float(input())
price_fruits = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

fruits_income = price_fruits * fruits_kg
vegetables_income = price_vegetables * vegetables_kg

total_income = fruits_income + vegetables_income
total_income_euro = total_income / 1.94

print(f'{total_income_euro:.2f}')
