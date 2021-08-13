lengths = {1:1}


def collatz(n):
    if n%2 == 0:
        return n/2
    return 3*n+1


def get_length(n):
    if n in lengths:
        return lengths[n]
    return 1 + get_length(collatz(n))


longest = 1
for i in range(2, 1000000):
    lengths[i] = get_length(i)
    if lengths[i] > lengths[longest]:
        longest = i

print(longest)