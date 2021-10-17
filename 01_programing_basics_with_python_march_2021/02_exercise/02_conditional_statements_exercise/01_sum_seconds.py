#input

time_first = int(input())
time_secound = int(input())
time_third = int(input())

#calculations

total_time = time_first + time_secound + time_third

minutes = total_time // 60
secounds = total_time % 60

#output

if secounds < 10:
    print(f"{minutes}:0{secounds}")
else:
    print(f"{minutes}:{secounds}")
