from typing import List
# binary search
# good for *sorted* array with O(log(n)) time complexity
# Given a sorted array and a target value, find the index of the target t

# e.g. {1,2}, t = 1, returns 0
# 0. li = 0, ri = 1
# 1. mid = (0+1)//2 = 0, arr[0] == 1, return 1

# e.g. {1,2}, t = 2, returns 1
# 0. li = 0, ri = 1
# 1. mid = (0+1)//2 = 0, arr[0] = 1 <2, go to right half
# 2. mid = (1+1)//2 = 1, arr[1] = 2 == 2, return 1

# e.g. {1,2}, t = 3, returns -1
# 0. li = 0, ri = 1
# 1. mid = (0+1)//2 = 0, arr[0] = 1 <3, go to right half
# 2. mid = (1+1)//2 = 1, arr[1] = 2 <3, go to right half
# 3. li = 1+1, ri = 1, li>ri, return -1

# e.g. {1,2}, t = -1, returns -1
# 0. li = 0, ri = 1
# 1. mid = (0+1)//2 = 0, arr[0] = 1 >-1, go to left half
# 2. li = 0, ri = mid-1 = -1, li>ri, return -1


def binary_search(arr, li, ri, t):
    # as long as the range between li and ri is an effective one
    # when li==ri, it's essentially one element
    if li <= ri:
        mid = (li+ri)//2
        # print(mid)
        if t == arr[mid]:
            return mid
        elif t < arr[mid]:
            return binary_search(arr, li, mid-1, t)  # mid has to move so it doesn't get stuck with one element at either end
        else:
            return binary_search(arr, mid+1, ri, t)
    else:
        return -1

test = [1,2]
binary_search(test, 0, len(test)-1, 1)

############ slightly simiplified ##########
def binary_search1(arr: List[int], target: int) -> int:
    def helper(l, r):
        if l > r:
            return -1
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
        return helper(l,r)
    return helper(0, len(arr)-1)  # 1

binary_search1([1,2,3],4)

# 1, the initial rindex is the rightmost an index can go
# it needs to be the last VALID index

############ simiplified, without recursion ##########
# Note this approach only returns the index of the input array. 
# If binary search is used as part of an algorithm that needs to search different parts of a mother array
# this approach would not output the correct index of the mother array
# See example below for when binary search a rotated array
def binary_search2(arr: List[int], target: int) -> int:
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1
binary_search2([1,2,3,4],4)



###################################
# find element in a sorted but rotated array
# e.g. given arr={5, 6, 7, 8, 9, 10, 1, 2, 3}, target=9; return 4

# pivot is i where arr[i]>arr[i+1]
# This approach is not recommended due to multiple scenarios
# Use the alternative approach find_pivot1
def find_pivot(arr, start, end):
    '''
    start and end are the indices of the two ends of the subarray.
    '''
    # empty array
    if start > end:
        return None
    # single element array
    if start == end:
        return start
    # if the first element of the array is less than the last,
    # then the array is not rotated
    if arr[0] < arr[end]:
        return -1
    
    mid = (start+end)//2
    # these two scenarios take care of comparing mid to its neighbor
    # as the recursive is not going to include mid
    # when mid is the pivot
    if arr[mid] > arr[mid+1]:
        return mid
    # when mid-1 is the pivot
    if arr[mid-1] > arr[mid]:
        return mid-1
    # when pivot is to the right of mid, everything on the left is smaller than pivot
    if arr[start] < arr[mid]:
        return find_pivot(arr, mid+1, end)
    # when pivot is to the left of mid, 
    return find_pivot(arr, start, mid-1)
    
t1 = [1,2,5,6,10,11]
t2 = [10,11,1,2,5,6]
# t1 = []
find_pivot(t2,0,len(t2)-1)



####### alt approach findPivot #######
# the key is to realize that the arr can be translated into
# a series of continuous False and continue True values
# e.g. [4,1,2,3] -> [False, True, True, True] if we test arr[i] <= arr[-1]
# Then the problem is to find the first True index
def find_pivot1(arr: List[int]) -> int:
    l = 0
    r = len(arr)-1
    last = arr[-1]
    bound = -1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] <= last:
            bound = mid
            r = mid-1
        else:
            l = mid+1
    return bound

def pivot_binary_search(arr, target):
    pivot = find_pivot1(arr)

    if arr[pivot] == target:
        return pivot
    if arr[0] <= target:
        return binary_search(arr, 0, pivot-1, target)
    return binary_search(arr, pivot+1, len(arr)-1, target)


if __name__ == "__main__":
    test = [5,6,1,2,3,4]
    print(pivot_binary_search(test, 2))