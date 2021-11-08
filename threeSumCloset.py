# threeSumCloset
# https://leetcode.com/problems/3sum-closest/
# Given an array of nums, return the closet sum of three numbers to target
# Brute force solution: compare all possible 3 sum combo with target, 
# has time complexity O(n^3) = n * (n-1) * (n-2)
# Optimized solution: sort nums first, then for each anchor num (there are n-2 of them),
# there is only n-1 combos to go through, time complexity O(n^2) = (n-2) * (n-1)
# You will need to go through all n-2 numbers as anchor 
# because the question asks for closet, and the numbers in the array can be both +/- 

# [1] set anchor numbers, ie the first number heading a 3sum combo
# leaving two numbers out in the end because they cannot be anchors
# [2] the second num is the one next to anchor, and the third num is the last/largest in the array
# [3] record the current solution being the closet to target
# [4] if current 3-sum is larger than target, then nums[k] the larget number needs to be smaller
# if current 3-sum is less than target, then nums[j] needs to be bigger
# if current 3-sum is equal to target, if it would have already been returned

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        cur_sol = sum(nums[:3])  # [3]
        for i in range(len(nums)-2):  # [1]
            j, k = i+1, len(nums)-1  # [2]
            while j < k:  # j cannot be = k because we need 3 numbers
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == target:
                    return cur_sum  # [4]
                if abs(cur_sum - target) < abs(cur_sol - target):  # [3]
                    cur_sol = cur_sum
                if cur_sum > target:  # [4] 
                    k -= 1
                else:
                    j += 1  # [4]
        return cur_sol
        
        