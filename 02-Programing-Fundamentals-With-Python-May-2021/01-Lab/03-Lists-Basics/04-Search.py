count_of_sentences = int(input())
key_word = input()

list_of_sentences = []
list_of_key_word_sentences = []

for count in range(1, count_of_sentences + 1):
    current_sentence = input()
    list_of_sentences.append(current_sentence)
    if key_word in current_sentence:
        list_of_key_word_sentences.append(current_sentence)

print(list_of_sentences)
print(list_of_key_word_sentences)
