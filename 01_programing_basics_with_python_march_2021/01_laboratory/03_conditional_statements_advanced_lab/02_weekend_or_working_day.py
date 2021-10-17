# input

weekday = input()

# output

if weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" or weekday == "Friday":
    print("Working day")
elif weekday == "Saturday" or weekday == "Sunday":
    print("Weekend")
else:
    print("Error")
