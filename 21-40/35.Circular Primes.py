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
circular_primes = []

def is_circular(prime):
    prime_string = str(prime)
    for r in range(len(prime_string) - 1):
        prime_string = prime_string[1:] + prime_string[0]
        if int(prime_string) not in prime_set:
            return False
    return True

for prime in primes:
    if is_circular(prime):
        circular_primes.append(prime)

print(circular_primes)
print(len(circular_primes))
print(is_circular(19))


