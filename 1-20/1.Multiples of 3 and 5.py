def sum_divisible(target, n):
    p = target//n
    return n*p*(p+1)/2


print(sum_divisible(999, 3) + sum_divisible(999, 5) - sum_divisible(999, 15))
