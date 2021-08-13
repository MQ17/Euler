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

prime_set = set(primes)

truncatable_primes = []

def is_truncatable(prime):
    string = str(prime)
    for i in range(1, len(string)):
        if int(string[i:]) not in prime_set or int(string[:-i]) not in prime_set:
            return False
    return True

for prime in primes:
    if is_truncatable(prime):
        truncatable_primes.append(prime)
    if len(truncatable_primes) == 15:
        break

print(sum(truncatable_primes[4:]))


