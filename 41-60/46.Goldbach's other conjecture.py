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

primes = {2}
for i in range(sieve_length):
    if sieve[i]:
        primes.add(2*i+3)


def GoldbachWrong(n):
    if n in primes:
        return False

    base = 1
    twice_square = 2*base**2
    while twice_square < n:
        if n-twice_square in primes:
            # print(n-twice_square)
            return False

        base += 1
        twice_square = 2 * base ** 2

    return True


i = 35
while True:
    if(GoldbachWrong(i)):
        print(i)
        break
    i += 2