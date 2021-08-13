import math

# Sieve
limit = 1000000
sieve_length = (limit-3)//2
cross_limit = (math.floor(math.sqrt(limit))-1)//2
sieve = [True]*sieve_length

for i in range(cross_limit):
    if sieve[i]:
        for j in range(2*i*(i+3)+3, sieve_length, 2*i+3):
            sieve[j] = False

primes = [2]
for i in range(sieve_length):
    if sieve[i]:
        primes.append(2*i+3)

prime_set = set(primes)

prime = 0
max_count = 0
for i in range(100):
    cut_primes = primes[i:]
    total = 0
    count = 0
    for prime in cut_primes:
        total += prime
        count += 1
        if total in prime_set and count > max_count:
            max_count = count
            prime = total
            print(i, max_count, prime)

