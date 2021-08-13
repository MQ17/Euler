def concatenated_product(integer, n):
    product = ''
    for i in range(1, n):
        product += str(integer*i)
    return product


def is_pandigital(product):
    return len(product) == 9 and set(product) == set('123456789')

max_pandigital = 0
for n in range(2,10):
    for i in range(1, 10000):
        product = concatenated_product(i, n)
        if is_pandigital(product) and int(product) > max_pandigital:
            max_pandigital = int(product)


print(max_pandigital)