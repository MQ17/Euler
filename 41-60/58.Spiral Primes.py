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

print(primes)

def is_prime(n):
    sqrt_n = math.floor(math.sqrt(n))
    for prime in primes:
        if prime > sqrt_n:
            return True
        if n % prime == 0:
            return False

i = 1
prime_count = 0
space = 1
while True:
    space += 4
    square = (2*i+1)**2
    possible_primes = [square-2*i, square-4*i, square-6*i]
    for possible_prime in possible_primes:
        if is_prime(possible_prime):
            prime_count += 1
    percentage = prime_count/space
    print(prime_count, space, percentage)
    if percentage < 0.10:
        print(2*i+1)
        break
    i += 1
print(len(primes))
