# https://leetcode.com/problems/132-pattern/
# [Understand] 
# i<j<k means to maintain the order of the array
# a_j < a_k < a_j means the second value needs to be bigger than the third value
# [Strategy]
# Because we are only returning boolean value, we don't have to be concerned about 
# qualifying subsequence whose first element is not the smallest in the array
# i.e. if we have nums = [-1,1,4,2], then [1,4,2] is an answer, but we only need to 
# focus on [-1,4,2] where the first element is the smallest of the array.


from typing import List
def find132pattern(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False
    stack = []
    curmin = nums[0]  # current min seens so far
    for num in nums[1:]:
        if num < curmin:
            curmin = num
        while stack and num > stack[-1][0]:
            if num < stack[-1][1]:
                return True
            else:
                stack.pop()
        stack.append([curmin, num])  # [1]
    return False

# [1] what's appended is either [a,b] where a < b or [a,a] where num is the most recent cur min
# in the latter scenario, it will be popped out in the while loop.

test = [[1,2,3,4], [3,2,1,4], [3,1,4,2], [1,3,2], [1,2], [3,3,3]]
for t in test:
    print(t, find132pattern(t))

