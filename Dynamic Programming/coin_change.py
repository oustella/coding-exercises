# Given a list of coin denominations, 
# return the minimum number of coins needed to reach the target amount

def coin_change(coins, target):
    # dp[i] is the min number coins that add up to amount i
    dp = [float("inf") for _ in range(target+1)]
    dp[0] = 0
    for i in range(target+1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i-coin]+1, dp[i])
    return dp[target] if dp[target] < float('inf') else -1 


coin_change([1,2,5], 10)
