last_ten = 1
for i in range(7830457):
    last_ten *= 2
    last_ten %= 10000000000

print((28433*last_ten+1)%10000000000)