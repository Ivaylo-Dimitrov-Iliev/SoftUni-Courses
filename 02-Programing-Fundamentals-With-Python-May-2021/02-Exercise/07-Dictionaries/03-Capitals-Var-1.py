countries = input().split(", ")
capitals = input().split(", ")

countries_dictionary = dict(zip(countries, capitals))

print({f"{country} -> {capital}" for country, capital in countries_dictionary.items()})
