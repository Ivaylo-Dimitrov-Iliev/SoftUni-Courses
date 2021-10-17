#input

import math

record_in_secounds = float(input())
distance = float(input())
time_for_one_meter = float(input())

#calculations

theoretical_swim_time = distance * time_for_one_meter
total_delay = math.floor(distance / 15) * 12.5
real_swim_time = theoretical_swim_time + total_delay

#output


if record_in_secounds > real_swim_time:
    print(f"Yes, he succeeded! The new world record is {real_swim_time:.2f} seconds.")
else:
    need_time = real_swim_time - record_in_secounds
    print(f"No, he failed! He was {need_time:.2f} seconds slower.")
