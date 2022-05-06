# 456. 132 Pattern
# https://leetcode.com/problems/132-pattern/
# Given an array of n integers nums, a 132 pattern is a subsequence of three integers 
# nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise, return false.

# [Understand] 
# i<j<k means to maintain the order of the array
# a_j < a_k < a_j means the second value needs to be bigger than the third value
# [Strategy]
# Because we are only returning boolean value, we don't have to be concerned witth 
# qualifying subsequence whose first element is not the smallest in the array
# i.e. if we have nums = [-1,1,4,2], then [1,4,2] is an answer, but we only need to 
# focus on [-1,4,2] where the first element is the smallest of the array.


from typing import List
def find132pattern(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False
    stack = []
    curmin = nums[0]  # current min seen so far
    for num in nums[1:]:
        if num < curmin:
            curmin = num
        while stack and num > stack[-1][0]: # [2] 
            if num < stack[-1][1]:
                return True
            else:
                stack.pop()
        stack.append([curmin, num])  # [1]
    return False

# [1] what's appended is either [a,b] where a < b or [a,a] where num is the most recent cur min
# in the latter scenario, it will be popped out in the while loop. 
# But no pair where a > b will be appended as a candidate.
# [2] pass on a necessary condition here. If num < stack[-1][0], the candidate doesn't get popped
test = [[1,2,3,4], [3,2,1,4], [3,1,4,2], [1,3,2], [1,2], [3,3,3]]
for t in test:
    print(t, find132pattern(t))

