#min sub sum
# max sub multi
# backpack problem with max profit
from typing import List
# Given an array, return the max sum of a contiguous subarray
# This is an inplace strategy with space O(N) and time O(N)
# At each index of the array, find the max up to that point
# it boils down to whether to include the max sum from the previous index
# https://leetcode.com/problems/maximum-subarray/

def returnMaxSum(array: List) -> int:
    for i in range(1, len(array)):
        array[i] = max(array[i], array[i]+array[i-1])
    return max(array)

if __name__ == "__main__":
    test = [-2,1,-3,4,-1,2,1,-5,4]
    print(returnMaxSum(test))

