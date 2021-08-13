from fractions import Fraction

nth = 100 - 1
a = [1]*nth
k = 2
for i in range(1, nth, 3):
    a[i] = k
    k += 2
print(a)
e = Fraction(a[-1], 1)
a = a[-2::-1] + [2]
print(a)
print(e)
for constant in a:
    e = constant + 1/e

print(e)
print(float(e))
print(sum(int(digit) for digit in str(e.numerator)))