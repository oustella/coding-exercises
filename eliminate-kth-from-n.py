# CodeSignal question
# eliminate kth number from n numbers until one number is left.
# return the eliminated strings in order


def eliminateK(arr, k):
    output = []
    if k == 1:
        output = arr[:-1]  # output the original array in order except the last element
    else:
        while len(arr) >= k:  # while the array is not shorter than k
            # print(arr)  # print out what's left in the array for debugging
            pointer = k - 1  # make life easier by creating a pointer index
            output.append(arr[pointer])  # the kth element goes to output
            arr = arr[pointer+1:] + arr[:pointer]  # shortening the array. start from right to k and stop before k

        # print('enter second step')  # debugging
        while 1 < len(arr) < k:  # when the array has become shorter than k but still have more than 1 left.
            # print(arr)  # debugging
            pointer = k % len(arr) - 1  # the remainder is what goes out
            output.append(arr[pointer])
            arr = arr[pointer+1:] + arr[:pointer]  # shortening the arr

    return output


test = [1, 2, 3, 4, 5]
eliminateK(test, 1)
eliminateK(test, 2)
eliminateK(test, 3)
eliminateK(test, 7)
