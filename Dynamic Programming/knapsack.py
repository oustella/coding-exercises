# A 1999 study of the Stony Brook University Algorithm Repository showed that, 
# out of 75 algorithmic problems, the knapsack problem was the 19th most popular 
# and the third most needed after suffix trees and the bin packing problem.
# https://en.wikipedia.org/wiki/Knapsack_problem
# What's the maximum value the knapsack can have?

# 1-0 Knapsack Problem: Each item can only be used once 
# Input: w = {1,2,3}, v = {10,14,40}, maximum weight W = 6, n number of items

# Strategy:
# [1] if the weight of the current item with weight w[i-1] and value v[i-1] 
#   is less than the current weight the bag allows
#   it can be added to the bag
#   e.g. when i = 1, the 1st item corresponds to w[0] and v[0] (1-1=0)
# [2] whether to add the current item depends on
# if adding this item can achieve greater value than keeping the knapsack as is.
# the current knapsack value with this item = the previous max value without the weight of this item
# E.g. when the bag currently allows 3 pounds, and you are evaluating if adding a 2lb item (the second item in the offering, i=2)
# the bag value has two possibiliies: 
#   a. the max value when your bag weighs 3-2 = 1lb + the 2lb-item value: dp[1][1]+v[1]
#   b. the max value as is, without adding this item, i.e. when the bag weighs 2 pounds: dp[1][3]
# [3] if the current item weighs more than current bag allows
# the max bag value is the same as not adding this item dp[1][3]
def knapsack(w, v, W, n):
    '''
    w: the weight array
    v: the value array
    W: maximum allowed weight
    n: total number of available items
    '''
    if W==0 or n==0:
        return 0
    # dp[i][j] is the max value when the bag weight is j pound 
    # and HAVE THE OPPORTUNITY to use up to i items, i.e. whether to use depends
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        for accum_w in range(W+1):
            if i == 0 or accum_w == 0:  # when not using any item or the bag allows no weight
                continue
            # the state matrix row and the index for the weight array is off by 1
            # so w[i-1] and dp[i] is for the adding the same ith item
            elif w[i-1] <= accum_w:  #[1]
                # remember dp[i-1] is the state before allowing the ith item
                dp[i][accum_w] = max(dp[i-1][accum_w], v[i-1]+dp[i-1][accum_w-w[i-1]])  #[2]
            else:  #[3]
                dp[i][accum_w] = dp[i-1][accum_w]
    print(dp)
    return dp[n][W]

# Unbounded knapsack problem
# If each item can be used unlimited times
# This can be translated to the coin change program
# where the weight limit becomes the target value
# and the max value becomes the min # coins
def unbounded_knapsack(w, v, W, n):
    '''
    w: the weight array
    v: the value array
    W: maximum allowed weight
    n: total number of available items
    '''
    if W==0 or n==0:
        return 0
    # dp[i][j] is the max value when the bag weight is j pound 
    # and HAVE THE OPPORTUNITY to use up to i items, i.e. whether to use all of them depends
    dp = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(n+1):
        for accum_w in range(W+1):
            if i == 0 or accum_w == 0:  # when not using any item or the bag allows no weight
                continue
            # the state matrix row and the index for the weight array is off by 1
            # so w[i-1] and dp[i] is for the adding the same ith item
            elif w[i-1] <= accum_w:  #[1]
                # remember dp[i-1] is the state before allowing the ith item
                dp[i][accum_w] = max(dp[i-1][accum_w], v[i-1]+dp[i][accum_w-w[i-1]])  #[2]
            else:  #[3]
                dp[i][accum_w] = dp[i-1][accum_w]
    print(dp)
    return dp[n][W]

def unbounded_knapsack1(weights, values, weight_limit):
    dp = [-float("inf") for _ in range(weight_limit+1)]  
    dp[0] = 0  
    for w in range(1, weight_limit+1):  
        for i in range(len(weights)): 
            if w - weights[i] >= 0: 
                dp[w] = max(dp[w-weights[i]]+values[i], dp[w])  
    return dp[weight_limit] if dp[weight_limit] > -float('inf') else -1  

# optimized space complexity
# [5] dp[w] is the maxium value when the bag allows (up to) w weight and using up to i items
# [6] checking for weight limit up to current max weight item
# essentially the same as #[1] above: making sure the current item weighs less than what's allowed
def knapsack4(weights, values, weight_limit):
    dp = [0 for i in range(weight_limit + 1)]  # Making the dp array
    for i in range(len(weights)):  # taking first i items
        for w in range(weight_limit, weights[i]-1, -1):  #[6]
            dp[w] = max(dp[w], dp[w-weights[i]]+values[i])  #[5]
            print(w, i, dp)
    return dp[weight_limit]  # returning the maximum value of knapsack


if __name__ == "__main__":
    val = [4, 5, 8]
    wt = [1, 3, 7]
    W = 7
    n = len(val)
    # knapsack(wt, val, W, n)
    # unbounded_knapsack(wt, val, W, n)
    # unbounded_knapsack1(wt, val, W)
    knapsack4(wt, val, W)
            