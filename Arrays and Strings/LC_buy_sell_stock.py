# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(prices):
    # if only one day price, then cannot trade, return 0
    if len(prices) == 1:
        return 0
    min_pur = prices[0]  # initiate minimum purchase price
    target = 0  # initiate target profit
    # starting from the second day
    for i in range(1, len(prices)):
        # record the lowest price by ith day
        min_pur = min(min_pur, prices[i])
        # is selling today going to make a greater profit than the previous target
        target = max(target, prices[i]-min_pur)
    return target

# requires O(n) time complexity
# strategy is to record the min price as you traverse through the array

# extension: when you can trade more than once to achieve max profits
def maxProfit_multi(prices):
    # if only one day price, then cannot trade, return 0
    if len(prices) == 1:
        return 0
    i = 0
    tot_profit = 0
    # only traverse the array once because the sell must happen after the buy
    # i.e. the array is a temporal array that has direction
    while i < len(prices)-1:  # make sure i+1 covers the last element but doesn't exceed it
        # starting from the beginning find the first local minima
        # keep advancing i if the next element is smaller than the current
        while i < len(prices)-1 and prices[i+1] <= prices[i]:
            i += 1
        # if out of the above loop i is already at the end
        # then no need to find a sell price because the price has been going down
        if i == len(prices) - 1:
            print('The price has been going down during this whole period.')
            break
        # record the local minima
        buy = i  # i corresponds to the last time prices[i+1] smaller than prices[i]
        # advance to the next day as the first candidate for sell
        i += 1
        # advance i if the price keeps going up
        while i < len(prices)-1 and prices[i+1] > prices[i]:
            i += 1
        sell = i
        i += 1
        # print(prices[buy], prices[sell])
        tot_profit += prices[sell] - prices[buy]
    return tot_profit


# requires O(n) time complexity
# strategy is to record the min price as you traverse through the array




if __name__=='__main__':
    test = [100,200,3,6,10,20,20, 100]
    print(test)
    print('one trade', maxProfit(test))
    print('multi trade', maxProfit_multi(test))

    test = [5,4,3,2,1]
    print(test)
    print(maxProfit(test))
    maxProfit_multi(test)
