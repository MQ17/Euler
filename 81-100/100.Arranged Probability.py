import math

def is_triangle(n):
    determinant = 8*n+1
    return round(math.sqrt(determinant))**2 == determinant

size = 1000000000001
n = math.ceil(math.sqrt(size*(size-1)/2))
while True:
    product = n*(n-1)
    if is_triangle(product):
        print(n)
        break
    n += 1