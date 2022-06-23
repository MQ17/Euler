#https://oeis.org/A143714
import math

def is_square(n):
    return n == math.isqrt(n) ** 2

def cuboid_pairs(n):
    cnt = 0
    for b in range(1, n+1):
        for a in range(1, b+1):
           if is_square((a+b)**2 + n**2):
               cnt += 1
    return cnt

cnt = 0

m = 1
while True:
    cnt += cuboid_pairs(m)
    if cnt > 1000000: #1000000:
        print(m)
        break
    m += 1

# for m in range(10):
#     count = 0
#     for a in range(1,m+1):
#         for b in range(1, a+1):
#             for c in range(1, b+1):
#                 if is_square(a**2 + (b + c)**2):
#                     count += 1
#     print(count)