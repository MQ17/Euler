def length(n):
    length = 0
    letters = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4,
               3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens_letters = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]

    ones = n%10
    teens = n%100

    #First Two digits
    if teens<20:
        length += letters[teens]
    else:
        tens = teens//10
        length += tens_letters[tens]
        length += letters[ones]

    #Check for AND
    if n>99:
        length += letters[(n - teens) // 100]
        length += 7
        if teens>0:
            length += 3
    return length


print(sum([length(i) for i in range(1,1000)]) + 11)