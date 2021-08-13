f = open("p089_roman.txt")
saved = 0
roman = {'I':1, 'V':5,
         'X':10, 'L':50,
         'C':100, 'D':500,
         'M':1000, '\n':0}

shortests = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
# Only technically needed the length of the shortest roman, but oh well
def shortest_roman(n):
    roman = 'M'*(n//1000)
    roman += shortests[n//100%10].replace('X', 'M').replace('I', 'C').replace('V', 'D')
    roman += shortests[n//10%10].replace('X', 'C').replace('I', 'X').replace('V', 'L')
    roman += shortests[n%10]
    return roman

count = 0
for numeral in f:
    number = 0
    for i in range(len(numeral)-1):
        digit = roman[numeral[i]]
        next_digit = roman[numeral[i+1]]
        if next_digit > digit:
            number -= digit
        else:
            number += digit
    # print(numeral, len(numeral), shortest_roman(number), len(shortest_roman(number)),number)
    count += len(numeral) - len(shortest_roman(number)) - 1

print(count)