mackerel_price = float(input())     # skumriya
toy_price = float(input())          # caca
kg_bonito = float(input())          # palamud
kg_horse_mackerel = float(input())  # safrid
kg_mussels = int(input())           # midi

bonito_price = mackerel_price * 1.60
horse_mackerel_price = toy_price * 1.80
mussels_price = 7.50

bonito_cost = bonito_price * kg_bonito
horse_mackerel_cost = horse_mackerel_price * kg_horse_mackerel
mussels_cost = mussels_price * kg_mussels

bill = bonito_cost + horse_mackerel_cost + mussels_cost

print(f'{bill:.2f}')
