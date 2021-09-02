def partition(nums, left_idx, right_idx):
    # pivot = nums[(left_idx+right_idx)//2]
    # pivot = nums[left_idx-1]
    # pivot = nums[right_idx]
    pivot = nums[left_idx]
    while True:
        while nums[left_idx] < pivot and left_idx <= right_idx:
            left_idx += 1
        # print(left_idx)
        while nums[right_idx] > pivot and right_idx >= left_idx:
            right_idx -= 1
        if left_idx >= right_idx:
            return right_idx
        nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
        # print(nums)
        left_idx += 1
        right_idx -= 1
        
def quick_sort_helper(nums, left_idx, right_idx):
    print(nums)
    if left_idx >= right_idx:
        return
    pivot_idx = partition(nums, left_idx, right_idx)
    print('pivot', pivot_idx)
    if left_idx < pivot_idx:
        quick_sort_helper(nums, left_idx, pivot_idx)
    if right_idx > pivot_idx + 1:
        quick_sort_helper(nums, pivot_idx + 1, right_idx)

def quick_sort(nums):
    quick_sort_helper(nums, 0, len(nums) - 1)

# nums = [6,12,4,3,5]
nums = [6,5,4,3]
# partition(nums, 0, len(nums)-1)
# print('partitioned', nums)

quick_sort(nums)
print(nums)