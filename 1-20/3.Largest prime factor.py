x = 600851475143
for i in range(1, x):
    if 600851475143%i == 0:
        if i == x:
            print(x)
        x /= i
