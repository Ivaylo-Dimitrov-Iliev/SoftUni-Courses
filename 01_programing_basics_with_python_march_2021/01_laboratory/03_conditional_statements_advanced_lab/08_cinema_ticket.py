# input

day = input()

# variable

ticket_cost = 0

# statements

if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    ticket_cost = 12
elif day == 'Wednesday' or day == 'Thursday':
    ticket_cost = 14
elif day == 'Saturday' or day == 'Sunday':
    ticket_cost = 16

# output

print(ticket_cost)
