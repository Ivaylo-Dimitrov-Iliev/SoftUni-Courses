employee_1_efficiency = int(input())
employee_2_efficiency = int(input())
employee_3_efficiency = int(input())

total_count_of_customers = int(input())

total_count_of_serviced_customers_per_hour = employee_1_efficiency + \
                                             employee_2_efficiency + \
                                             employee_3_efficiency

time_counter = 0

for current_customer in range(1, total_count_of_customers + 1, total_count_of_serviced_customers_per_hour):
    time_counter += 1
    if time_counter % 4 == 0:
        time_counter += 1

print(f"Time needed: {time_counter}h.")
