def pentagonal(n):
    return n*(3*n-1) // 2


divisors = {}


def sum_divisors(n):
    if n in divisors:
        return divisors[n]
    divisors[n] = 0
    for k in range(1, n+1):
        coeff = -1 if k%2==0 else 1
        for t in [pentagonal(k), pentagonal(-k)]:
            if (n-t) > 0:
                divisors[n] += coeff*sum_divisors(n-t)
            elif (n-t) == 0:
                divisors[n] += coeff*n
    return divisors[n]

def proper_sum(n):
    return sum_divisors(n)-n

# chain_lengths = {}
# used = set()
# for i in range(1000001):
#     if i in used:
#         continue
#     less_million = True
#     chain = set()
#     element = i
#     while element not in chain:
#         chain.add(element)
#         element = proper_sum(element)
#         if element > 1000000:
#             less_million = False
#             break
#
#     length = len(chain) if less_million else -1
#     for item in chain:
#         chain_lengths[item] = length
#         used.add(item)
#
# print(chain_lengths)