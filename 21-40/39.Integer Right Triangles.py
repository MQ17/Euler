import math

max_triplets = 0
max_s = 0

for s in range(12, 1001, 2):
    triplets = 0
    s2 = s/2
    mlimit = math.ceil(math.sqrt(s2))
    for m in range(2, mlimit):
        if s2%m == 0:
            sm = s2/m
            while sm%2 == 0:
                sm /= 2

            if m%2 == 1:
                k = m+2
            else:
                k = m+1

            while k < 2*m and k <= sm:
                if sm%k == 0 and math.gcd(k, m) == 1:
                    d = s2/(k*m)
                    n = k-m
                    a = d*(m*m-n*n)
                    b = 2*d*m*n
                    c = d*(m*m+n*n)
                    # triplets.append((a, b, c))
                    triplets += 1
                    break
                k += 2

    if triplets > max_triplets:
        max_triplets = triplets
        max_s = s

print(max_s)

