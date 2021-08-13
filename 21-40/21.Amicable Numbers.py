import math

# Sieve
limit = 10001
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


def combinations(factors, index=0):
    if len(factors) == 1:
        return [primes[index]**i for i in range(factors[0]+1)]
    subset_displacement = 1
    while factors[subset_displacement] == 0:
        subset_displacement += 1
    subset = combinations(factors[subset_displacement:], index+subset_displacement)
    return [(primes[index]**i)*item for i in range(factors[0]+1) for item in subset]

# divisors = combinations(prime_factorize(220))
# divisors.sort()
# print(divisors)
amicable_sum = 0
sums = {1:-1}
for n in range(2, 10000):
    divisor_sum = sum(combinations(prime_factorize(n))) - n
    sums[n] = divisor_sum
    if divisor_sum < n and sums[divisor_sum] == n:
        amicable_sum += n + divisor_sum


print(sums[220])
print(amicable_sum)
