import math
import time

start = time.time()
# Sieve
limit = 9163
sieve_length = (limit-3)//2
cross_limit = (math.floor(math.sqrt(limit))-1)//2
sieve = [True]*sieve_length

for i in range(cross_limit):
    if sieve[i]:
        for j in range(2*i*(i+3)+3, sieve_length, 2*i+3):
            sieve[j] = False

primes = []
for i in range(sieve_length):
    if sieve[i]:
        primes.append(2*i+3)
primes.pop(1)
print(primes)

def is_prime(n):
    sqrt_n = math.floor(math.sqrt(n))
    for prime in primes:
        if prime > sqrt_n:
            return True
        if n % prime == 0:
            return False


def is_prime_pair_set(number1, prime_pair_set):
    for number2 in prime_pair_set:
        if not is_prime(int(str(number1) + str(number2))) or not is_prime(int(str(number2) + str(number1))):
            return False
    return True


def find_prime_pair_set(n):
    if n == 1:
        return [[i+1, [primes[i]]] for i in range(len(primes))]
    lower_prime_pair_sets = find_prime_pair_set(n-1)
    prime_pair_sets = []
    for lower_prime_pair_set in lower_prime_pair_sets:
        for i in range(lower_prime_pair_set[0], len(primes)):
            if is_prime_pair_set(primes[i], lower_prime_pair_set[1]):
                prime_pair_sets.append([i+1, lower_prime_pair_set[1] + [primes[i]]])
    return prime_pair_sets

print(find_prime_pair_set(5))
print(time.time() - start)

#     for a in range(len(primes)):
#         prime_pair_set = [primes[a]]
#         for b in range(a+1, len(primes)):
#             if is_prime_pair_set(primes[b], prime_pair_set):
#                 prime_pair_set.append(primes[b])
#                 return prime_pair_set
#
# print(find_prime_pair_set())
# print(is_prime_pair_set(3, [2]))




# def is_prime_pair_set(number_set):
#     for combo in combos:
#         number1 = str(number_set[int(combo[0])])
#         number2 = str(number_set[int(combo[1])])
#         if not is_prime(int(number1 + number2)) or not is_prime(int(number2 + number1)):
#             return False
#     return True
#
# prime_pair_set = []
# min_sum = 999999999999999
# for a in range(len(search_space)):
#     for b in range(a+1, len(search_space)):
#         for c in range(b+1, len(search_space)):
#             for d in range(c+1, len(search_space)):
#                 for e in range(d+1, len(search_space)):
#                     numbers = [search_space[a], search_space[b], search_space[c], search_space[d], search_space[e]]
#                     if is_prime_pair_set(numbers) and sum(numbers) < min_sum:
#                         min_sum = sum(numbers)
#                         prime_pair_set = numbers