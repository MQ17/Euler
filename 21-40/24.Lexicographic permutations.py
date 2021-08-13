import math

position = 999999
digits = 10
permutation = ""
numerals = [str(n) for n in range(digits)]
for digit in range(1, digits+1):
    other_digits = digits-digit
    factorial = math.factorial(other_digits)
    position_value = position // factorial
    position %= factorial
    permutation += str(numerals.pop(position_value))

print(permutation)
