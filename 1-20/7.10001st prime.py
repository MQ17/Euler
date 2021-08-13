primes = [2]
n = 3


def is_prime(n):
    for prime in primes:
        if n%prime == 0:
            return False
    return True


while len(primes) < 10001:
    if is_prime(n):
        primes.append(n)
    n += 2

print(primes)
