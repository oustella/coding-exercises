# Count the number of times a given number x occurs in a sorted array
# Time complexity O(n)
# Increase the count by 1 when the middle value equals x
# Otherwise keeps searching values to the left and to the right of mid

def num_occurences(arr, x):
    def helper(arr, x, start, end):
        if start > end:
            return 0
        mid = (start + end) // 2
        if arr[mid] > x:
            return helper(arr, x, start, mid-1)
        if arr[mid] < x:
            return helper(arr, x, mid+1, end)
        return 1 + helper(arr, x, start, mid-1) + helper(arr, x, mid+1, end)
    return helper(arr, x, 0, len(arr)-1)

print(num_occurences([2,2,3,5,6,7], 2))
print(num_occurences([2,3,5], 7))