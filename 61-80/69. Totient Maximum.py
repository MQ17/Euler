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

primes = [2]
for i in range(sieve_length):
    if sieve[i]:
        primes.append(2*i+3)

def prime_factors(n):
    factors = []
    for prime in primes:
        if n%prime == 0:
            factors.append(prime)
        while n%prime == 0:
            n /= prime
        if n == 1:
            return factors


def totient(n):
    phi = n-1
    for prime in prime_factors(n):
        phi -= phi//prime
    return phi
print(totient(1))
max_n = 0
max_phi = 0
for i in range(2, 1000001):
    if i/totient(i) > max_phi:
        max_n = i
        max_phi = i/totient(i)
        print(max_n, max_phi)

print(max_n)