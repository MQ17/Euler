n = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]


def combinations(n, coins):
    print(n, coins)
    if n == 0 or coins == [1]:
        return 1
    total = 0
    current_coin = coins[-1]
    for i in range(n//current_coin+1):
        total += combinations(n-current_coin*i, coins[:-1])

    print(n, coins, n//current_coin+1, total)
    return total


print(combinations(n, coins))
