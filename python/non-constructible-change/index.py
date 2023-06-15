def nonConstructibleChange(coins):
    coins.sort()
    sum = 0
    print(coins)
    for coin in coins: 
        if coin <= (sum + 1):
            sum += coin
        else: 
            return sum + 1
    return sum + 1