sequence_of_cards = input().split()
count_of_shuffles = int(input())


half_cars = len(sequence_of_cards) // 2

for current_shuffle in range(1, count_of_shuffles + 1):
    first_half_of_cards = sequence_of_cards[0:half_cars]
    second_half_of_cards = sequence_of_cards[half_cars:]
    shuffled_cards = []
    for current_card_in_shuffle in range(0, half_cars):
        shuffled_cards.append(first_half_of_cards[current_card_in_shuffle])
        shuffled_cards.append(second_half_of_cards[current_card_in_shuffle])
    sequence_of_cards = shuffled_cards

print(sequence_of_cards)
