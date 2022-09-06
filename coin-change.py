# Returns the minimum number of coins that sum up to value
def min_coins(coins, value):
    dp = [float('inf')]*(value + 1)
    dp[0] = 0
    
    for partial in range(1, value + 1):
        for coin in coins:
            if coin <= partial:
                dp[partial] = min(dp[partial], 1 + dp[partial - coin])

    return dp[value]
    
print(min_coins(list(range(1, 5)), 30))
print(min_coins(list(range(1, 4)), 4))
print(min_coins(list(range(1, 21)), 15))
