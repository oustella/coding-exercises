# MergeSort
def mergeSort(arr):
    if len(arr) > 1:  # merge sort until only one element in the arr
        m = len(arr)//2  # middle place of the array
        l_arr = arr[:m]  # left array
        r_arr = arr[m:]  # right array
        mergeSort(l_arr)  # repeat all on the left is sorted and merged
        mergeSort(r_arr)
        # merge happens after the array has been broken into individual elements
        # so that the mereg can happen at every level of the stack  
        merge(arr, l_arr, r_arr)

        # print(l_arr, r_arr, arr)  # this line helps understand the recursive process
    return arr

def merge(arr, l_arr, r_arr):  # O(n) time, one pass
    """
    merge two arrays so the merged array is sorted
    in place operation to update the main arr
    """
    i = j = k = 0  # i pointer for l_arr, j for r_arr, k for new arr 'merged'
    # merged = [None]*(len(l_arr)+len(r_arr))  # for standalone function 
    while i < len(l_arr) and j < len(r_arr):  # pointers go to the last element
        if l_arr[i] <= r_arr[j]:  # if element in the left array is <= the one in the right
            arr[k] = l_arr[i]  # put it in the new array
            i += 1  # progress the left pointer to see if it is still smaller than the current one on the right
        else:
            arr[k] = r_arr[j]
            j += 1
        k += 1
    if i < len(l_arr):  # if there are still elements left in the left array
        arr[k:] = l_arr[i:]
    else:  # it's either the left pointer arrives first or the right. They cannot arrive at the same time
        arr[k:] = r_arr[j:]

########## simplified version ########
def merge_sort(nums):
    # the base case, the stopping condition
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_sorted = merge_sort(nums[:mid])
    right_sorted = merge_sort(nums[mid:])
    return merge(left_sorted, right_sorted)

def merge(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    if arr1[0] <= arr2[0]:
        return [arr1[0]] + merge(arr1[1:], arr2)
    else:
        return [arr2[0]] + merge(arr1, arr2[1:])


if __name__ == '__main__':
    test1 = [5,1,6,84,2]
    test2 = [1]
    test3 = [1,6,4,6,3,6]

    # mergeSort(test1)
    # mergeSort(test2)
    # mergeSort(test3)

    merge_sort(test1)
    merge_sort(test2)
    merge_sort(test3)




 # other sorting algorithms to implement:
 # bubble sort
 # insertion sort O(n^2)
 # heap sort O(nlogn)

 # selection sort O(n^2)
 # The selection sort algorithm sorts an array by repeatedly finding the minimum element 
 # (considering ascending order) from unsorted part and putting it at the beginning. 
 # The algorithm maintains two subarrays in a given array.
 