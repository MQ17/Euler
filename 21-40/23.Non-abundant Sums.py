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


def sum_of_divisors(n):
    divisor_sum = 1
    m = n
    for p in primes:
        j = p

        while m % p == 0:
            j *= p
            m /= p

        divisor_sum *= j-1
        divisor_sum /= p-1

        if m == 1:
            break

    return divisor_sum - n

def is_abundant(n):
    return sum_of_divisors(n) > n

abundant_numbers = {}

for i in range(2, 28124):
    if is_abundant(i):
        abundant_numbers[i] = True

print(abundant_numbers)

sum = 0 
for i in range(1, 28124):
    for a in abundant_numbers:
        if i-a in abundant_numbers:
            print(i, a, i-a)
            break
        elif a > i:
            sum += i
            break

print(sum)