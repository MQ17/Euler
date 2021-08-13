import math


def is_square(n):
    return round(math.sqrt(n))**2 == n


def get_next(x, numerator, denominator):
    next_numerator = (x - denominator**2)//numerator
    aplus = math.floor(numerator/(math.sqrt(x)-denominator))
    next_denominator = aplus*next_numerator - denominator
    return next_numerator, next_denominator


def get_cycle_length(x):
    count = 1
    initial_fraction = (1, math.floor(math.sqrt(x)))
    fraction = get_next(x, *initial_fraction)
    while fraction != initial_fraction:
        fraction = get_next(x, *fraction)
        count += 1
    return count


total = 0
for i in range(10001):
    if is_square(i):
        continue
    print(i, get_cycle_length(i))
    if get_cycle_length(i)%2 == 1:
        total += 1
print(total)
# print(get_next(23, 1, 4))
# print(get_next(23, 7, 3))
# print(get_next(23, 2, 3))
# print(get_next(23, 7, 4))


