import math

total = 0
for i in range(3, 2540161):
    if sum(math.factorial(int(digit)) for digit in str(i)) == i:
        total += i

print(total)