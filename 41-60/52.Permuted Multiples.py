def same_digits(a, b):
    a = list(str(a))
    a.sort()
    b = list(str(b))
    b.sort()
    return a == b


def permuted_multiple(n):
    for i in range(1, 7):
        if not same_digits(n, i*n):
            return False
    return True

x = 1
while True:
    if permuted_multiple(x):
        print(x)
        break
    x += 1

