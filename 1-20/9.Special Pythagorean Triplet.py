import math

for a in range(1, 500):
    for b in range(a, 500):
        c = math.sqrt(a**2+b**2)
        if c.is_integer() and a+b+c == 1000:
            print(a*b*c)
            print(a,b,c)
