# https://leetcode.com/problems/sliding-window-maximum/

from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        big = deque()
        ans = []
        for i, num in enumerate(nums):
            # kick out previous seen numbers that are smaller than current num
            while big and nums[big[-1]] <= num:
                big.pop()
            # record current num b/c without it, list `big` will not start to fill
            # also serves in case the cur_num is the max of the current sliding window    
            big.append(i)
            # if the distance between current i and leftmost in big is greater than k
            # the leftmost has fallen out of bounds.
            # only need to check once, b/c i moves one at a time
            if i - big[0] >= k:
                big.popleft()
            # start recording answers starting the first k numbers    
            if i + 1 >= k:
                # note the leftmost is the current window max
                ans.append(nums[big[0]])
        return ans

