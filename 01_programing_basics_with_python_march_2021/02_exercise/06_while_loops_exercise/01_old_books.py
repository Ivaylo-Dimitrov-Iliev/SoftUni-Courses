# input

book_name = input()

# variables

book_count = 0
is_book_found = False

# secondary input

current_book = input()

# loop

while current_book != 'No More Books':
    if current_book == book_name:
        is_book_found = True
        print(f'You checked {book_count} books and found it.')
        break

    book_count += 1
    current_book = input()

if not is_book_found:
    print('The book you search is not here!')
    print(f'You checked {book_count} books.')
