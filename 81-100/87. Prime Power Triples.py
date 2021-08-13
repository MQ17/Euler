import math

# Sieve
limit = 7073
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


count = set()
for a in primes:
    for b in primes:
        if b > 368:
            break
        for c in primes:
            if c > 84:
                break
            if a**2+b**3+c**4 < 50000000:
                count.add(a**2+b**3+c**4)

print(len(count))



print(count)