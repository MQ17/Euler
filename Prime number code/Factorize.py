import math

# Sieve
limit = 10000
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


def prime_factorize(n):
    exponents = []
    for prime in primes:
        exponents.append(0)
        while n%prime == 0:
            n /= prime
            exponents[-1] += 1
        if n == 1:
            return exponents

def combinations(things, n):
    if n == 0:
        return ['']
    combos = []
    for i in range(len(things)):
        subthings = things.copy()
        thing = subthings.pop(i)
        for subcombo in combinations(subthings, n-1):
            combos.append(thing + subcombo)
    return combos

def is_prime(n):
    sqrt_n = math.floor(math.sqrt(n))
    for prime in primes:
        if prime > sqrt_n:
            return True
        if n % prime == 0:
            return False


def is_permutation(a, b):
    a_list = list(str(a))
    a_list.sort()
    b_list = list(str(b))
    b_list.sort()
    return a_list == b_list