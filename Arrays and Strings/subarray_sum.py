# Given an array and a target
# Return the beginning and end (exclusive) of the subarray
# whose sum equals the target
# There's only one solution to the target sub-sum.

# Strategy: sum(0,j) - sum(0,i) = sum(i+1, j) (inclusive)
# sum(0,i) is called a prefix_sum
# When both sum(0,j) and sum(0,i) emerges, and their difference is the target
# We know the target's starting and ending indices
#%%
from typing import List
def subarray_sum(arr: List, target: int) -> List:
    prefix_sum = {0:0} #[2]
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement_val = cur_sum - target
        if complement_val in prefix_sum:
            return [prefix_sum[complement_val]+1-1, i+1] #[1]
        prefix_sum[cur_sum] = i+1
        print(prefix_sum)

#[1] prefix_sum[complement_val]+1 corresponds to the i+1 
# then -1 since the prefix_sum keeps track of everyone's index +1
# i+1 is because the question requires exclusive ending index
# while i is in the original array index, not to be confused with
# the index+1 in the prefix_sum lookup

#[2] starts the lookup with sum=0 when no element in the array is included
# this is for when the entire array adds up to the target
#%%
test = [1,2,3,14,6]
target = 5
print(subarray_sum(test, target))



# %%
