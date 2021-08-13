pentagon_numbers = []
pentagon_set = set()

for n in range(1, 10001):
    number = n*(3*n-1)/2
    pentagon_numbers.append(number)
    pentagon_set.add(number)

for i in range(10000):
    for j in range(i+1, 10000):
        a = pentagon_numbers[i]
        b = pentagon_numbers[j]
        if a+b in pentagon_set and b-a in pentagon_set:
            print(a, b, b-a)