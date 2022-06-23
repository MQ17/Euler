import math

def minimal_product_sum(k):
    max = 2
    while True:
        for i in range(max**k):
            sum = 0
            product = 1
            for j in range(k):
                digit = i % max + 1
                sum += digit
                product *= digit 
                i
            if summed == math.prod(numbers):
                return summed
        max += 1