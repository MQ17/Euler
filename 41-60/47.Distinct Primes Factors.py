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


dict_distinct = {}
def find_distinct_primes(n):
    if n in dict_distinct:
        return dict_distinct[n]
    distinct_primes = 0
    for prime in primes:
        if prime > n:
            break
        if n%prime == 0:
            distinct_primes += 1
    dict_distinct[n] = distinct_primes
    return distinct_primes


n = 210
while True:
    if find_distinct_primes(n) == find_distinct_primes(n+1) == find_distinct_primes(n+2) == find_distinct_primes(n+3) == 4:
        print(n)
        break
    n += 1
