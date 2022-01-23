#input

number_of_pages_in_current_book = int(input())
pages_for_one_hour = int(input())
available_days_for_reading = int(input())

#calculations

required_reading_hours = number_of_pages_in_current_book / pages_for_one_hour
required_reading_hours_per_day = required_reading_hours / available_days_for_reading

#output

print(required_reading_hours_per_day)
