# https://leetcode.com/problems/array-transformation/

test_arr = [2,1,2,1,1,2,2,1]

def test(arr):
    for i, num in enumerate(arr):
        if 1 <= i <= len(arr) -2:
            if num > arr[i-1] and num > arr[i+1]:
                return False
            elif num < arr[i-1] and num < arr[i+1]:
                return False
    return True


def transformArray(arr):
    while not test(arr):  # if the array does not meet testing criteria
        new_arr = []  # have to create a new arr so that each number can be judged by the existing array
        for i, num in enumerate(arr):
            if i == 0 or i == len(arr) - 1:  # head and tail stay unchanged
                new_arr.append(num)
            elif num > arr[i - 1] and num > arr[i + 1]:
                new_arr.append(num - 1)
            elif num < arr[i - 1] and num < arr[i + 1]:
                new_arr.append(num + 1)
            else:  # if a num is larger than one side and smaller than another side
                new_arr.append(num)
        arr = new_arr  # update existing arr with new and put to testing
    return arr


transformArray(test_arr)
