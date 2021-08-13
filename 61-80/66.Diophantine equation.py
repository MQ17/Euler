import math


def is_square(n):
    return round(math.sqrt(n))**2 == n


def get_next(x, numerator, denominator):
    next_numerator = (x - denominator**2)//numerator
    aplus = math.floor(numerator/(math.sqrt(x)-denominator))
    next_denominator = aplus*next_numerator - denominator
    return aplus, next_numerator, next_denominator


def get_continued_fraction(x):
    continued_fraction = [math.floor(math.sqrt(x))]
    initial_fraction = (1, continued_fraction[0])

    fraction = get_next(x, *initial_fraction)
    continued_fraction.append(fraction[0])
    while fraction[1:] != initial_fraction:
        fraction = get_next(x, *fraction[1:])
        continued_fraction.append(fraction[0])
    return tuple(continued_fraction)

p_answers = {}
def p(n, a):
    if n == 0:
        return a[0]
    elif n == 1:
        return a[1]*a[0] + 1
    elif (n, a) in p_answers:
        return p_answers[(n, a)]
    else:
        p_answers[(n, a)] = a[n]*p(n-1, a) + p(n-2, a)
        return p_answers[(n, a)]

# def p(n, a):
#     if n == 0:
#         return a[0]
#     elif n == 1:
#         return a[1]*a[0] + 1
#     else:
#         return a[n]*p(n-1, a) + p(n-2, a)


# If length of period m is even then (x,y) = (Pm-1, Qm-1) else, (P2m-1, Q2m-1)
def solve_pell(d):
    a = get_continued_fraction(d)
    m = len(a)-1
    if m%2 == 0:
        return p(m-1, a)
    else:
        a = a + a[1:]
        return p(2*m-1, a)


# print(solve_pell(13))
max_x = 0
max_d = 0
for i in range(2, 1001):
    if is_square(i):
        continue
    x = solve_pell(i)
    print(i, x)
    if x > max_x:
        max_x = x
        max_d = i

print(max_d)