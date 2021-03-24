# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(prices):
    # if only one day price, then cannot trade, return 0
    if len(prices) == 1:
        return 0
    min_pur = prices[0]
    target = 0
    for i in range(1, len(prices)):
        # record the lowest price by ith day
        min_pur = min(min_pur, prices[i])
        # is selling today going to make a greater profit than the previous target
        target = max(target, prices[i]-min_pur)
    return target

# requires O(n) time complexity
# strategy is to record the min price as you traverse through the array

if __name__=='__main__':
    test = [100,200,3,6,10,20]
    print(maxProfit(test))
