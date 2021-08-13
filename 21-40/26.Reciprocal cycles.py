max_length = 0
max_number = 0
for d in range(2, 1000):
    i = 0
    exp = 1
    reciprocals = {}
    while exp %d not in reciprocals:
        reciprocals[exp % d] = i
        i += 1
        exp *= 10
    length = i-reciprocals[exp%d]
    if length > max_length:
        max_length = length
        max_number = d

print(max_number)
