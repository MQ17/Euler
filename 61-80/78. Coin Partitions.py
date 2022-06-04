#https://pages.uoregon.edu/koch/PentagonalNumbers.pdf

def get_pentagonal(n):
    k = (n+1) // 2 if n %2 == 1 else -n // 2
    return k*(3*k-1) // 2 

def get_partitions(divisor):
    partitions = [1]
    while True:
        p_n = 0
        n = len(partitions)
        k = 1
        pent_num = 1 
        while pent_num <= n: 
            multiplier = 1 if (k-1)% 4 < 2 else -1
            p_n += multiplier*partitions[n-pent_num]
            k += 1
            pent_num = get_pentagonal(k)
        if p_n % divisor == 0:
            print(partitions)
            print(p_n)
            return len(partitions)
        partitions.append(p_n)

print(get_partitions(1000000))