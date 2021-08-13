def combinations(things, n):
    if n == 0:
        return [''.join(things)]
    combos = []
    for i in range(len(things)):
        subthings = things.copy()
        thing = subthings.pop(i)
        for subcombo in combinations(subthings, n-1):
            combos.append(thing + subcombo)
    return combos


pandigitals = set()
products1 = set()
products2 = set()
print(combinations(list('123456789'), 5))
for combo in combinations(list('123456789'), 5):
    product2x3 = int(combo[:2])*int(combo[2:5])
    multipland_digits_2x3 = list(str(product2x3))
    multipland_digits_2x3.sort()
    leftover_digits = list(combo[5:])
    leftover_digits.sort()

    if multipland_digits_2x3 == leftover_digits:
        pandigitals.add(product2x3)
        products1.add((int(combo[:2]), int(combo[2:5])))

    product1x4 = int(combo[:1])*int(combo[1:5])
    multipland_digits_1x4 = list(str(product1x4))
    multipland_digits_1x4.sort()

    if multipland_digits_1x4 == leftover_digits:
        pandigitals.add(product1x4)
        products2.add((int(combo[:1]), int(combo[1:5])))

print(products1)
print(products2)
print(sum(pandigitals))


