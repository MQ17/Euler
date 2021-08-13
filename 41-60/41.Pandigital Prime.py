import math

# Sieve
limit = 100000
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


def is_prime(n):
    for prime in primes:
        if n%prime == 0:
            return False
    return True


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

def find_pandigital_prime():
    for n in range(9, 5, -1):
        for combo in combinations(list("987654321"[(9-n):]), n):
            if is_prime(int(combo)):
                print(combo, n)
                return combo

find_pandigital_prime()
