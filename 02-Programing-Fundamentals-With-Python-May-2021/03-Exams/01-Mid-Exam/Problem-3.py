deck_of_cards = input().split(":")

command = input()

new_deck_of_cards = []

while not command == "Ready":
    command_data_list = command.split()
    action = command_data_list[0]
    if action == "Add":
        card_name = command_data_list[1]
        if card_name in deck_of_cards:
            new_deck_of_cards.append(card_name)
        else:
            print("Card not found.")
    elif action == "Insert":
        card_name = command_data_list[1]
        index = int(command_data_list[2])
        if card_name in deck_of_cards and index in range(len(new_deck_of_cards)):
            new_deck_of_cards.insert(index, card_name)
        else:
            print("Error!")
    elif action == "Remove":
        card_name = command_data_list[1]
        if card_name in new_deck_of_cards:
            new_deck_of_cards.remove(card_name)
        else:
            print("Card not found.")
    elif action == "Swap":
        card_1_name = command_data_list[1]
        card_2_name = command_data_list[2]
        index_1 = new_deck_of_cards.index(card_1_name)
        index_2 = new_deck_of_cards.index(card_2_name)
        new_deck_of_cards[index_1], new_deck_of_cards[index_2] = \
            new_deck_of_cards[index_2], new_deck_of_cards[index_1]
    elif action == "Shuffle":
        new_deck_of_cards = new_deck_of_cards[::-1]

    command = input()

print(" ".join(new_deck_of_cards))
