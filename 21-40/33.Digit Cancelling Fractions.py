import math

fractions = []
for denominator in range(10, 100):
    for numerator in range(10, denominator):
        d = math.gcd(numerator, denominator)
        simplified_numerator = int(numerator / d)
        simplified_denominator = int(denominator / d)
        leftover_numerator_index = str(numerator).find(str(simplified_numerator))
        if leftover_numerator_index != -1 and len(str(simplified_numerator)) == 1:
            cancelled_numerator = str(numerator)[1-leftover_numerator_index]
            leftover_denominator_index = str(denominator).find(str(simplified_denominator))
            if leftover_denominator_index != -1 and len(str(simplified_denominator)) == 1:
                cancelled_denominator = str(denominator)[1-leftover_denominator_index]
                if cancelled_numerator == cancelled_denominator and (numerator%10 != 0 or denominator%10 != 0):
                    print(numerator, denominator, simplified_numerator, simplified_denominator)
                    fractions.append((numerator, denominator))

print(fractions)
