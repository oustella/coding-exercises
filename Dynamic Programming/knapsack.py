# A 1999 study of the Stony Brook University Algorithm Repository showed that, 
# out of 75 algorithmic problems, the knapsack problem was the 19th most popular 
# and the third most needed after suffix trees and the bin packing problem.
# https://en.wikipedia.org/wiki/Knapsack_problem

# 1-0 Knapsack Problem: Each item can only be used once 
# Input: w = {1,2,3}, v = {10,14,40}, maximum weight W = 6, n number of items
def knapsack(w, v, W, n):
    '''
    w: the weight array
    v: the value array
    W: maximum allowed weight
    n: total number of available items
    '''
    if W==0 or n==0:
        return 0
    # each row corresponds to the index of each item
    # each col is the accumulating weights up to W
    dp = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for accum_w in range(W+1):
            if i == 0 or accum_w == 0:
                dp[i][accum_w] = 0
            # the state matrix row and the index for the weight array is off by 1
            # so w[i-1] and dp[i] is for the adding the same ith item
            elif w[i-1] <= accum_w:
                # dp[i-1] is the state before adding the ith item, v[i-1] corresponds to w[i-1]
                dp[i][accum_w] = max(dp[i-1][accum_w], v[i-1]+dp[i-1][accum_w-w[i-1]])
            else:
                dp[i][accum_w] = dp[i-1][accum_w]
    return dp[n][W]

if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    knapsack(wt, val, W, n)
            