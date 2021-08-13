import math

def count_divisors(n):
    count = 0
    for i in range(1, math.floor(math.sqrt(n))):
        if n%i == 0:
            count +=2
    return count

x = 1
while True:
    triangle = x*(x+1)/2
    if count_divisors(triangle) > 500:
        print(triangle)
        break
    x += 1