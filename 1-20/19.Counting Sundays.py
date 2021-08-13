# 365 mod 7 = 1
# 31 mod 7 = 3
# 30 mod 7 = 2
# 29 mod 7 = 1
# 28 mod 7 = 0
#January 1st, 1901 was a tuesday
import math
num_sundays = [2, 1, 1, 3, 1, 2, 2]
num_sundays_leap = [3, 1, 1, 2, 2, 1, 2]

sundays = 0
current_day = 2
for i in range(1,101):
    if i%4 != 0:
        sundays += num_sundays[current_day]
        current_day = (current_day + 1) % 7
    else:
        sundays += num_sundays_leap[current_day]
        current_day = (current_day + 2) % 7
print(sundays)