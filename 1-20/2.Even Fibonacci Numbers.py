# x odd y even
def next_even(x, y):
    return x+2*y, 2*x+3*y

sum = 0
current = (1, 2)
while(current[1] < 4000000):
    sum += current[1]
    current = next_even(*current)

print(sum)
