def square_digit_sum(n):
    return sum(int(digit)**2 for digit in str(n))


results = {1:1, 89:89}
count = 0
for i in range(1, 10000000):
    n = i
    while n not in results:
        n = square_digit_sum(n)
    results[i] = results[n]
    if results[i] == 89:
        count += 1

print(count)