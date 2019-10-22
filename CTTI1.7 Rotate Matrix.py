# not working yet.. 10/22/2019
# 1.7
# this solution creates another array instead of doing it in place
def rotateArray(arr):
    """
    values in the first column become the first row
    [i,j] --> [j, r-i]
    :param arr: nxn array in the form of list of lists[[1,2,3],[],[]]
    :return: nxn array rotated 90 degrees clockwise
    """
    n = len(arr)
    r = n - 1
    # new_arr = [0 * n] * n  # NOTE: this will create unintended behavior where if you change [i][j], the value on the other rows will change too.
    new_arr = [[0 for r in range(n)] for c in range(n)]
    for i in range(n):
        for j in range(n):
            new_i = j
            new_j = r - i
            new_arr[new_i][new_j] = arr[i][j]
    return new_arr

def rotateArray(arr):
    """
    values in the first column become the first row
    [i,j] --> [j, r-i]
    :param arr: nxn array in the form of list of lists[[1,2,3],[],[]]
    :return: nxn array rotated 90 degrees clockwise
    """
    n = len(arr)
    r = n - 1
    for i in range(n):
        for j in range(n):
            new_i = j
            new_j = r - i
            arr[new_i][new_j] = arr[i][j]
    print(arr)

testArr = [[1,2,3], [4,5,6], [7,8,9]]

rotateArray(testArr)


testArr[:]=zip(*testArr[::-1])

x = 1
~x
