import math


def is_permutation(a, b):
    a_list = list(str(a))
    a_list.sort()
    b_list = list(str(b))
    b_list.sort()
    return a_list == b_list


length_groups = []
n = 1
cube = 1
for l in range(1, 12):
    length_group = []
    while len(str(cube)) == l:
        length_group.append(cube)
        n += 1
        cube = n**3
    length_groups.append(length_group)

print(length_groups)

def find_family(n):
    for length_group in length_groups:
        used = set()
        for i in range(len(length_group)):
            root = length_group[i]
            if root in used:
                continue
            family = [root]
            for j in range(i+1, len(length_group)):
                possible_perm = length_group[j]
                if is_permutation(root, possible_perm):
                    family.append(possible_perm)
                    used.add(possible_perm)
            if len(family) == n:
                print(root, family)
                return root

find_family(5)


