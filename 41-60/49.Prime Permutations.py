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

primes = []
for i in range(sieve_length):
    if sieve[i] and len(str(2*i+3)) == 4:
        primes.append(2*i+3)

prime_set = set(primes)

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


prime_permutations = []
for prime in primes:
    permutation_set = set()
    string = str(prime)
    combos = combinations(list(string), 4)
    for combo in combos:
        if int(combo) in prime_set:
            permutation_set.add(int(combo))
            primes.remove(int(combo))
            prime_set.remove(int(combo))
    if len(permutation_set) > 2:
        prime_permutations.append(permutation_set)

for permutation in prime_permutations:
    perm = list(permutation)
    perm.sort()
    for a in range(len(perm)):
        for b in range(a+1, len(perm)):
            for c in range(b+1, len(perm)):
                if perm[c]-perm[b] == perm[b]-perm[a]:
                    print(perm[a],perm[b],perm[c])

