# input

command = input()

# variables

student_tickets = 0
standard_tickets = 0
kid_tickets = 0

# loop

while command != 'Finish':
    seats = int(input())
    sold_tickets = 0
    while sold_tickets < seats:
        ticket_type = input()
        if ticket_type == 'student':
            student_tickets += 1
            sold_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
            sold_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1
            sold_tickets += 1
        elif ticket_type == 'End':
            break
    hall_occupancy = sold_tickets / seats * 100
    print(f'{command} - {hall_occupancy:.2f}% full.')
    command = input()

else:
    total_tickets = student_tickets + standard_tickets + kid_tickets
    percentage_student_tickets = student_tickets / total_tickets * 100
    percentage_standard_tickets = standard_tickets / total_tickets * 100
    percentage_kid_tickets = kid_tickets / total_tickets * 100
    print(f'Total tickets: {total_tickets}')
    print(f'{percentage_student_tickets:.2f}% student tickets.')
    print(f'{percentage_standard_tickets:.2f}% standard tickets.')
    print(f'{percentage_kid_tickets:.2f}% kids tickets.')
