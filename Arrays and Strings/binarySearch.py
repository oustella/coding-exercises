from typing import List
# binary search
# good for sorted array with O(log(n)) time complexity
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


def binarySearch(arr, li, ri, t):
    # as long as the range between li and ri is an effective one
    # when li==ri, it's essentially one element
    if li <= ri:
        mid = (li+ri)//2
        # print(mid)
        if t == arr[mid]:
            return mid
        elif t < arr[mid]:
            return binarySearch(arr, li, mid-1, t)  # mid has to move so it doesn't get stuck with one element at either end
        else:
            return binarySearch(arr, mid+1, ri, t)
    else:
        return -1

test = [1,2]
binarySearch(test, 0, len(test)-1, 1)

############ simiplified ##########
def binary_search(arr: List[int], target: int) -> int:
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

binary_search([1,2,3],4)

# 1, the initial rindex is the rightmost an index can go
# it needs to be the last VALID index

############ simiplified, without recursion ##########
def binary_search(arr: List[int], target: int) -> int:
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
    

binary_search([1,2,3],4)


###################################
# find element in a sorted but rotated array
# e.g. given arr={5, 6, 7, 8, 9, 10, 1, 2, 3}, target=9; return 4

def pivotBinarySearch(arr, n, t):
    pivot = findPivot(arr, 0, n-1)

    if arr[pivot] == t:
        return pivot
    if arr[0] <= t:
        return binarySearch(arr, 0, pivot-1, t)
    return binarySearch(arr, pivot+1, n-1, t)

# pivot is i where arr[i]>arr[i+1]
def findPivot(arr, start, end):
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
        return findPivot(arr, mid+1, end)
    # when pivot is to the left of mid, 
    return findPivot(arr, start, mid-1)
    
t1 = [1,2,5,6,10,11]
t2 = [10,11,1,2,5,6]
# t1 = []
findPivot(t1,0,len(t1)-1)
pivotBinarySearch(t1, len(t1),1)


####### alt approach #######

def find_min_rotated(arr: List[int]) -> int:
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

find_min_rotated(t1)