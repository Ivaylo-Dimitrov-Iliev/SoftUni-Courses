favorite_genres = input().split(" | ")

command = input()

while not command == "Stop!":
    command_data_list = command.split()
    action = command_data_list[0]
    genre_1 = command_data_list[1]
    if action == "Join":
        if genre_1 not in favorite_genres:
            favorite_genres.append(genre_1)
    elif action == "Drop":
        if genre_1 in favorite_genres:
            favorite_genres.remove(genre_1)
    elif action == "Replace":
        genre_2 = command_data_list[2]
        if genre_1 in favorite_genres and genre_2 not in favorite_genres:
            favorite_genres = [genre_2 if el == genre_1 else el for el in favorite_genres]

    command = input()

print(" ".join(favorite_genres))
