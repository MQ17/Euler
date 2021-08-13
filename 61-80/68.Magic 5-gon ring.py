from itertools import permutations
import operator

def is_magic(perm):
    total = perm[4] + perm[0] + perm[9]
    for i in range(4):
        if perm[i] + perm[i+1] + perm[i+5] != total:
            return False
    return True

max_perm = 0

for perm in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    if 10 in perm[:5]:
        continue
    if is_magic(perm):
        start = min(enumerate(perm[5:]), key=operator.itemgetter(1))[0]
        string = ''
        for i in range(start, start-5, -1):
            i = i%5
            string += str(perm[i+5]) + str(perm[(i+1)%5]) + str(perm[i])
        print(perm, string, max_perm)
        if int(string) > max_perm:
            print("hallo", perm)
            max_perm = int(string)

print(max_perm)