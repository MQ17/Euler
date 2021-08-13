def reverse_add(n):
    return n + int(str(n)[::-1])


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_lychrel(n):
    for i in range(50):
        n = reverse_add(n)
        if is_palindrome(n):
            return False
    return True

total = 0
for i in range(10000):
    if is_lychrel(i):
        total += 1

print(total)