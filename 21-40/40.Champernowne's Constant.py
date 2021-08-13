def d(n):
    i = 1
    numbers = 9
    length = 9
    while n>length:
        n -= length

        i += 1
        numbers *= 10
        length = numbers*i

    displacement = (n-1)/i #zero indexing
    current_number = numbers/9 + displacement
    digit_number = (n-1)%i
    return int(str(current_number)[digit_number])

product = 1
for i in range(7):
    product *= d(10**i)

print(product)