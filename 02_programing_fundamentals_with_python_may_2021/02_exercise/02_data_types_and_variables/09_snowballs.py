import sys

number_of_snowballs = int(input())

best_snowball_value = 0
the_snowball_snow = 0
the_snowball_time = 0
the_snowball_quality = 0

for current_snowball in range(1, number_of_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > best_snowball_value:
        best_snowball_value = snowball_value
        the_snowball_snow = snowball_snow
        the_snowball_time = snowball_time
        the_snowball_quality = snowball_quality

print(f"{the_snowball_snow} : {the_snowball_time} = {best_snowball_value:.0f} ({the_snowball_quality})")
