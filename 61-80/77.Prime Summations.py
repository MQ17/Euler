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

prime_set = set(primes)
dictionary = {}


def count_sums(last_digit, leftover):

    if leftover == 0:
        return 1
    elif (last_digit, leftover) in dictionary:
        return dictionary[(last_digit, leftover)]
    count = 0
    for next_digit in primes:
        if next_digit > min(last_digit, leftover):
            break
        count += count_sums(next_digit, leftover-next_digit)
    dictionary[(last_digit, leftover)] = count
    return count

def prime_sum(n):
    total = count_sums(n, n)
    if n in prime_set:
        total -= 1
    return total

for i in range(10000):
    print(i, prime_sum(i))
    if prime_sum(i) > 5000:
        break
