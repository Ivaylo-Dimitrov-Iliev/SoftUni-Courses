#input

animal = input()

#variable

animal_type = ""

#variable statements

if animal == "dog":
    animal_type = "mammal"

elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    animal_type = "reptile"

else:
    animal_type = "unknown"

# output

print(animal_type)
