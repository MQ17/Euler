import math

f = open("p099_base_exp.txt")
lines = [[int(number) for number in line.split(',')] for line in f.read().split('\n')]
print(lines)

max_power = 0
max_i = 0
for i in range(len(lines)):
    exponent = lines[i]
    power = math.log2(exponent[0])*exponent[1]
    if power > max_power:
        max_power = power
        max_i = i

print(max_i+1)
