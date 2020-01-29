# Given two sorted arrays of integers and an integer n, find the nth (0-based) element of their sorted union.
# https://app.codesignal.com/challenge/rbwtuZjSG8zJQszCz


# Solution 1
def twoArraysNthElement(array1, array2, n):
    p1 = 0
    p2 = 0
    sorted_arr = []
    count = 0
    while p1 < len(array1) and p2 < len(array2) and count < n:
        if array1[p1] <= array2[p2]:
            sorted_arr.append(array1[p1])
            p1 += 1
        else:
            sorted_arr.append(array2[p2])
            p2 += 1
        count += 1
        if count == n+ 1:
            return sorted_arr[-1]
        print(p1, p2)
    sorted_arr.extend(array1[p1:]) if p1 < len(array1) - 1 else sorted_arr.extend(array2[p2:])
    print(sorted_arr)
    return sorted_arr[n]


# Solution 2. Shorter. Void the need of keeping the sorted array.
def twoArraysNthElement(array1, array2, n):
    p1 = 0
    p2 = 0
    c = 0
    while p1 < len(array1) and p2 < len(array2):
        if c == n:  # if n digits have been sorted, return the next digit whichever is smaller
            return min(array1[p1], array2[p2])
        else:
            p1 += 1 if array1[p1] <= array2[p2] else p2 += 1  # move along the pointers
            c+= 1  # increase the counts of sorted digits
    # if one array is used up, return the n-c th element from the current pointer position of the leftover array
    return array2[p2+n-c] if p2 < len(array2) else array1[p1+n-c]