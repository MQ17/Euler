from functools import cmp_to_key

f = open("p079_keylog.txt")
codes = f.read().split('\n')[:-1]
larger_numbers = [(i, set()) for i in range(10)]


for line in codes:
    larger_numbers[int(line[0])][1].add(line[1])
    larger_numbers[int(line[0])][1].add(line[2])
    larger_numbers[int(line[1])][1].add(line[2])

larger_numbers.sort(key=lambda x: len(x[1]), reverse=True)
print(larger_numbers)
print(''.join(str(group[0]) for group in larger_numbers))
#then remove 4 and 5
