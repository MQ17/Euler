import math

def factorial_sum(n):
   return sum(math.factorial(int(digit)) for digit in str(n))

count = 0
l = 1000000
chains = {}
for i in range(0, l):
    next = factorial_sum(i)
    if next in chains:
        index = chains[next].find(chain)
        if index == -1:
            chain = [i] + chains[next]
        else:
            chain = [i] + chains[next][:index]
    else:
        chain = [i]
        while next not in chain:
            chain.append(next)
            next = factorial_sum(next)
    if len(chain) == 60:
        count += 1
        print(chain)

print(count)