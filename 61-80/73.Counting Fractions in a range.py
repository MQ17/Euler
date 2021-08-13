from fractions import Fraction
import math


def mediant(a, b):
    return Fraction(a.numerator+b.numerator, a.denominator+b.denominator)

def fraction_count(l, q, h, d):
    if q.denominator > d:
        return 0
    lower_q = mediant(l, q)
    upper_q = mediant(q, h)
    return fraction_count(l, lower_q, q, d) + fraction_count(q, upper_q, h, d) + 1

def farey(n):
    # fractions = []
    count = 0
    (a, b, c, d) = (0, 1, 1, n)
    while c <= n:
        k = (n+b) // d
        (a, b, c, d) = (c, d, k*c-a, k*d-b)
        # fractions.append((a, b))
        if c/d >= 1/2:
            break
        elif c/d > 1/3:
            count += 1


    # print(fractions)
    return count

print(farey(12000))
# lower_bound = Fraction(0, 1)
# upper_bound = Fraction(1, 1)
# middle = mediant(lower_bound, upper_bound)
# print(fraction_count(lower_bound, middle, upper_bound, 1200))

