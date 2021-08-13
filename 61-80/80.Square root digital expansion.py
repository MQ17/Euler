import math
def not_square(n):
    return round(math.sqrt(n))**2 != n


def isqrt(n):
    x = n
    y = (x+1)//2
    while y < x:
        x = y
        y = (x+n//x)//2
    return x


def root_digits(n, length):
    n *= 100**(length-1)
    return isqrt(n)


def root_digits_sum(n, length):
    return sum(int(digit) for digit in str(root_digits(n, length)))

count = 0
for n in range(1, 100):
    if not_square(n):
        count += root_digits_sum(n, 100)

print(count)