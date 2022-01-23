countries = input().split(", ")
capitals = input().split(", ")

countries_dictionary = dict(zip(countries, capitals))

for country, capital in countries_dictionary.items():
    print(f"{country} -> {capital}")
