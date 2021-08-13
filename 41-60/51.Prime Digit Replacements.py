import math

# Sieve
limit = 1000000
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


def find_prime_family(n):
    for prime in primes:
        string = str(prime)
        for i in range(2**len(string)):
            family = []
            binary = str(bin(i))[2:]
            indicies = [index for index, element in enumerate(binary) if element == '1']

            for numeral in range(0, 10):
                new_string = list(string)
                for index in indicies:
                    new_string[index] = str(numeral)
                new_number = int(''.join(new_string))
                if new_number in prime_set and len(str(new_number)) == len(string):
                    family.append(new_number)

            if len(family) == n:
                print(prime, indicies)
                print(family)
                return prime, indicies


find_prime_family(8)
