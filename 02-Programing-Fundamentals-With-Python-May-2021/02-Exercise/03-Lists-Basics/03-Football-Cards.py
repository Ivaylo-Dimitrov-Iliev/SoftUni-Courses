sequence_of_cards = input().split()

team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

for card in sequence_of_cards:
    current_card = card.split("-")
    team_name = current_card[0]
    player_number = int(current_card[1])
    if team_name == "A" and player_number in team_a:
        team_a.remove(player_number)
    elif team_name == "B" and player_number in team_b:
        team_b.remove(player_number)
    if len(team_a) < 7 or len(team_b) < 7:
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if len(team_a) < 7 or len(team_b) < 7:
    print("Game was terminated")
