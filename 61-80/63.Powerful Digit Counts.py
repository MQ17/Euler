count = 0
for y in range(1,150):
    for x in range(1, 10):
        if len(str(x**y)) == y:
            count += 1

print(count)