import math

# def is_triangle(n):
#     p = math.floor(math.sqrt(2*n))
#     return p*(p+1)/2 == n

def is_triangle(n):
    p = (math.sqrt(1+8*n)-1)/2
    return p.is_integer()


def is_square(n):
    p = math.sqrt(n)
    return p.is_integer()


def is_pentagonal(n):
    p = (math.sqrt(1+24*n)+1)/6
    return p.is_integer()


def is_hexagonal(n):
    p = (math.sqrt(1+8*n)+1)/4
    return p.is_integer()


def is_heptagonal(n):
    p = (math.sqrt(9+40*n)+3)/10
    return p.is_integer()


def is_octagonal(n):
    p = (math.sqrt(4+12*n)+2)/6
    return p.is_integer()


for i in range(144,100000):
    n = i*(2*i-1)
    if is_triangle(n) and is_pentagonal(n):
        print(n)
        break

