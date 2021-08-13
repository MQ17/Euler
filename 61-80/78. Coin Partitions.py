def pentagonal(n):
    return n*(3*n-1) // 2

def get_partitions(limit):
    partitions = [1]
    for n in range(1, limit):
        partitions.append(0)
        for k in range(1, n+1):
            coeff = -1 if k%2==0 else 1
            for t in [pentagonal(k), pentagonal(-k)]:
                if (n-t) >= 0:
                    partitions[n] += coeff*partitions[n-t]
        partitions[n] %= 1000000
        print(partitions[n])
        if partitions[n] == 0:
            return n
    print(partitions)


print(get_partitions(1000000))