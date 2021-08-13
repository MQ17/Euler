import math

min_difference = 1
min_numerator = 0
for i in range(2, 1000001):

    numerator = math.floor(3/7*i)
    difference = 3/7-numerator/i

    if difference < min_difference and difference != 0.0:
        min_difference = difference
        min_numerator = numerator
        print("max!")
        print(numerator, i, difference)
