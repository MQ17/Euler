def pal(x):
    return str(x)[0:3] == str(x)[6:2:-1]


for x in range(999, 900, -1):
    for y in range(999, 900, -1):
        if pal(x*y):
            print(x*y)
