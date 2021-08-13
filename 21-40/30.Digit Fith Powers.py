total = 0
for n in range(2, 1000000):
    if n == sum(int(digit)**5 for digit in str(n)):
        total += n
        print(n)

print(total)