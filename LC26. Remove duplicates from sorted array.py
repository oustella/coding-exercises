# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates(self, nums: List[int]) -> int:
    # instantiate two pointers
    i = 0  # anchor pointer that tracks the last number we want to keep
    j = 1  # search pointer that looks for the next new, unique value
    while i < len(nums) and j < len(nums):
        if nums[i] != nums[j]:  # if the anchor and search values don't agree
            i += 1  # move the anchor pointer ahead 1
            nums[i] = nums[j]  # we want the anchor value to be updated to the search value
            j += 1  # move the search pointer ahead 1
        else:  # if the two values are repetitive
            j += 1  # we don't want the value at the search pointer, move it ahead
    return len(nums[:i+1])  # include all numbers where i arrives including the ith position
