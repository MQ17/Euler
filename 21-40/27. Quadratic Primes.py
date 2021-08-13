import math

# Sieve
limit = 1000001
sieve_length = (limit-3)//2
cross_limit = (math.floor(math.sqrt(limit))-1)//2
sieve = [True]*sieve_length

for i in range(cross_limit):
    if sieve[i]:
        for j in range(2*i*(i+3)+3, sieve_length, 2*i+3):
            sieve[j] = False

primes = {2}
for i in range(sieve_length):
    if sieve[i]:
        primes.add(2*i+3)

max_n = 0
max_a = 0
max_b = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while n*(n+a)+b in primes:
            n += 1
        if n > max_n:
            max_n = n
            max_a = a
            max_b = b

print(max_a*max_b)