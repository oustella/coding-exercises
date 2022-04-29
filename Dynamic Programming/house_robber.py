# House Robber
# You are given a street of houses, each with property worth value houses[i]
# You cannot loot two houses next to each other without getting caught
# What's the max value you can loot in one night?

# This is a classic sequence dp problem because you are asked to figure out the max value out of a sequence given some rules.
# The optimal substructure is if you loot house i, you cannot loot house i-1; if you don't loot house i, you can loot house i-1
# This translates into the recurrent relation in [1]
# The overlapping subproblem is that the cumulative max value is always contigent upon how much value you have looted prior 
# dp[i] is the best value (max in this case) for the sequence ending at index i

def maxLoot(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    dp = [0 for _ in range(len(nums))]  # [2]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i]+dp[i-2])  # [1]
    return dp[-1]

houses = [1,3,6,7,2]
print(maxLoot(houses))

houses = [5,8]
print(maxLoot(houses))


#%% 4/19/2022
from typing import List
def maxLoot(houses: List) -> int:
    dp = [0 for _ in range(len(houses))]
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])
    for i in range(2, len(houses)):
        dp[i] = max(houses[i] + dp[i-2], dp[i-1])
    return dp[-1]

houses = [2,7,9,3,1]
print(maxLoot(houses))
# %%
for i in range(2,2):
    print(i)
# %%
