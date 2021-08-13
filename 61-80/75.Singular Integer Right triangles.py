from math import gcd

# def cantor(a, b):
#     return (a+b)*(a+b+1)//2+b

def count_sieve(limit):
    triplet_counts = [0] * limit
    m = 2
    triplets = []
    while True:
        if m%2 == 0:
            n_start = 1
        else:
            n_start = 2
        for n in range(n_start, m, 2):
            if gcd(m, n) == 1:
                # print(m, n)
                (a, b, c) = (m*m-n*n, 2*m*n, m*m+n*n)
                s = a+b+c
                if s >= limit:
                    print(triplets)
                    return triplet_counts
                triplets.append((a, b, c, a+b+c))
                for wire_length in range(s, limit, s):
                    triplet_counts[wire_length] += 1
        m += 1

total = 0
counts = count_sieve(3000000)[:1500001]
print(counts[12])
print(counts[24])
print(counts[30])
print(counts[36])
print(counts[40])
print(counts[48])
print(counts[120])
for count in counts:
    if count == 1:
        total += 1

print(total)
