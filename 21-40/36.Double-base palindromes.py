total = 0
for i in range(1, 1000000):
    decimal_palindrome = str(i)[::-1] == str(i)
    binary_palindrome = str(bin(i))[:1:-1] == str(bin(i))[2:]
    if decimal_palindrome and binary_palindrome:
        total += i

print(total)