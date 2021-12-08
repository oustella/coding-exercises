# Given a list of coin denominations, 
# return the minimum number of coins needed to reach the target amount

# [1] dp needs to start with $0 and go up to $target so that target+1 positions
# use inf so that any solution is a real number smaller than inf
# so inf can be replaced by a solution when we take the min
# [2] zero coin required for zero dollar. Need this base scenario so that when i - coin = 0, it has 0 to be added to the count
# [4] need to try all the coin denominations to take out of the current amount i ** this is the most important step to implementation IMHO
# if current amount i - coint >= 0 it's a valid step
# [5] dp[i] is the min number coins that add up to amount i
# the recurrent relation is: the min number coins to add to amount i is either the coins needed to accumulate to $i - $coin plus 1 (the coin),
# or an existing solution that add to $i, whichever is smaller
# [6] if dp[target] still has +inf, it means no valid solution is available

def coin_change(coins, target):
    dp = [float("inf") for _ in range(target+1)]  # [1]
    dp[0] = 0  # [2] 
    for i in range(1, target+1):  # [3] start with $1 and ends with $target
        for coin in coins:  # [4]
            if i - coin >= 0: # [4]
                dp[i] = min(dp[i-coin]+1, dp[i])  # [5]
    return dp[target] if dp[target] < float('inf') else -1  # [6]


coin_change([1,2,5], 10)
