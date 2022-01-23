banned_words = input().split(", ")
text = input()

edited_text = [text.replace(banned_word, ("*" * len(banned_word))) for banned_word in banned_words]

print(f"{''.join(edited_text)}")
