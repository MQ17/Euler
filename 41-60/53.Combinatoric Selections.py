import math

def nCr(n,r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

total = 0
for n in range(10,101):
    for r in range(1, n):
        if nCr(n, r) > 1000000:
            total += 1

print(total)