import math

sum = 2
primes = []

def is_prime(n):
    for prime in primes:
        if n%prime == 0 :
            return False
        if prime > math.sqrt(n):
            break
    return True

for i in range(3, 2000000, 2):
    if is_prime(i):
        primes.append(i)
        sum += i

print(primes)
print(sum)
