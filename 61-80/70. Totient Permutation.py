import math
import time

start = time.time()

def is_permutation(a, b):
    a_list = list(str(a))
    a_list.sort()
    b_list = list(str(b))
    b_list.sort()
    return a_list == b_list

#sieve
min_ratio = 10
min_n = -1
limit = 10000000
phis = [n for n in range(limit)]
for n in range(2, limit):
    if phis[n] == n:
        for m in range(n, limit, n):
            phis[m] -= phis[m]//n
    ratio = n/phis[n]
    if is_permutation(n, phis[n]) and ratio<min_ratio:
        min_ratio = ratio
        min_n = n
        print(n, phis[n], ratio)

print(min_n)
