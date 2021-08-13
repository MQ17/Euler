import math
import time

start = time.time()

#sieve
limit = 1000001
phis = [n for n in range(limit)]
for n in range(2, limit):
    if phis[n] == n:
        for m in range(n, limit, n):
            phis[m] -= phis[m]//n

fraction_count = 0
for n in range(2, limit):
    fraction_count += phis[n]

print(fraction_count)

print(time.time() - start)
