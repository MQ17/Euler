def r(m, n):
    count = 0
    for a in range(m):
        for b in range(n):
            count += (m-a)*(n-b)
    return count


closest_difference = 1000000
area = 0
for a in range(1, 200):
    for b in range(a+1, 200):
        difference = r(a, b)-2000000
        if abs(difference) < abs(closest_difference):
            closest_difference = difference
            area = a*b
            print(2000000 + closest_difference)
            print(area)


