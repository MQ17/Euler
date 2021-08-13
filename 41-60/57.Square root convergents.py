from fractions import Fraction

# def convergent(n):
#     if n == 1:
#         return Fraction(1,2)
#     return Fraction(1, 2+convergent(n-1))
#
# for i in range(1,5):
#     print(convergent(i))

total = 0
convergents = [Fraction(1, 2)]
for i in range(1, 1000):
    next_convergent = Fraction(1, 2+convergents[-1])
    convergents.append(next_convergent)
    sqrt2 = 1 + next_convergent
    if len(str(sqrt2.numerator)) > len(str(sqrt2.denominator)):
        total += 1

print(convergents[7])
print(total)

