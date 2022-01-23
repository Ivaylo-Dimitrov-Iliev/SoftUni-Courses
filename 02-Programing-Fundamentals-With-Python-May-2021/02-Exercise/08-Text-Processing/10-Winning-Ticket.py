tickets = [x.strip() for x in input().split(",")]

for current_ticket in tickets:
    if len(current_ticket) == 20:
        left_half = current_ticket[:10]
        right_half = current_ticket[10:]

        left_half_is_match = False
        right_half_is_match = False

        matched_symbol_left = ""
        matched_symbol_right = ""

        for i in range(len(left_half)):
            if left_half[i] == "@" or left_half[i] == "#" or left_half[i] == "$" or left_half[i] == "^":
                matched_symbol_left = left_half[i]
                if left_half[i:i + 6] == matched_symbol_left:
                    left_half_is_match = True

        for j in range(len(right_half)):
            if right_half[j] == "@" or right_half[j] == "#" or right_half[j] == "$" or right_half[j] == "^":
                matched_symbol_right = right_half[j]
                if right_half[j:j + 6] == matched_symbol_right:
                    right_half_is_match = True

        if left_half_is_match and right_half_is_match and matched_symbol_left == matched_symbol_right:
            left_half_matches_count = left_half.count(matched_symbol_left)
            right_half_matches_count = right_half.count(matched_symbol_right)
            min_matches = min(left_half_matches_count, right_half_matches_count)
            if min_matches == 10:
                print(f"ticket \"{current_ticket}\" - {min_matches}{matched_symbol_left} Jackpot!")
            else:
                print(f"ticket \"{current_ticket}\" - {min_matches}{matched_symbol_left}")
        else:
            print(f"ticket \"{current_ticket}\" - no match")
    else:
        print("invalid ticket")
