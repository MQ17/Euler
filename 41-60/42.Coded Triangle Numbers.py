import math

f = open("p042_words.txt")
words = f.read()[1:-1].split('","')
def is_triangle(word):
    word_value = sum(ord(c)-64 for c in word)
    p = math.floor(math.sqrt(2*word_value))
    return p*(p+1)/2 == word_value

count = 0
for word in words:
    if is_triangle(word):
        count += 1

print(count)