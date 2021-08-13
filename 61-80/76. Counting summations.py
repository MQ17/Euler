dictionary = {}
def count_sums(last_digit, leftover):

    if leftover == 0:
        return 1
    elif (last_digit, leftover) in dictionary:
        return dictionary[(last_digit, leftover)]
    count = 0
    for next_digit in range(1, min(last_digit, leftover)+1):
        count += count_sums(next_digit, leftover-next_digit)
    dictionary[(last_digit, leftover)] = count
    return count

x = 5
print(count_sums(x, x)-1)