import time

start = time.time()

def combinations(things, n):
    if n == 0:
        return ['']
    combos = []
    for i in range(len(things)):
        subthings = things.copy()
        thing = subthings.pop(i)
        for subcombo in combinations(subthings, n-1):
            combos.append(thing + subcombo)
    return combos


primes = [1, 2, 3, 5, 7, 11, 13, 17]
def is_substring_divisible(s):
    for i in range(1,8):
        subnumber = int(s[i:i+3])
        if subnumber%primes[i] != 0:
            return False
    return True

total = 0
for pandigital in combinations(list("0123456789"), 10):
    if is_substring_divisible(pandigital):
        print(pandigital)
        total += int(pandigital)

print(total)
print(time.time()-start)


