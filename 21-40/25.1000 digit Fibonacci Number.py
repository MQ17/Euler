sequence = [0, 1]

while True:
    next = sequence[-1] + sequence[-2]
    if len(str(next)) == 1000:
        print(len(sequence))
        break
    else:
        sequence.append(next)

