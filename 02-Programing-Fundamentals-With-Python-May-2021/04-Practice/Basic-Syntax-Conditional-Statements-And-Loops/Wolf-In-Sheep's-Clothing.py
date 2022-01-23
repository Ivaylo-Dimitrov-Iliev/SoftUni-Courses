string = input()

list_of_animals = string.split(", ")
reversed_list_of_animals = list_of_animals[::-1]

phrase = ""

if reversed_list_of_animals[0] == "wolf":
    phrase = "Please go away and stop eating my sheep"

else:
    for animal in reversed_list_of_animals:
        if animal == "wolf":
            wolf_index_in_list = reversed_list_of_animals.index(animal)
            victim_sheep_position = wolf_index_in_list
            phrase = f"Oi! Sheep number {victim_sheep_position}! You are about to be eaten by a wolf!"

print(phrase)
