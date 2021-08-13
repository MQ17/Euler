smallest = 1
for i in range(2,20):
    cache = smallest
    while smallest%i != 0:
        smallest += cache

print(smallest)