# 1.7 Rotate a NxN 2D array clockwise by 90 degrees


# solution by CTTI, translated to Python by me
# rotate the numbers layer by layer
def rotateImage(a):
    n = len(a)
    # layer = 0
    for layer in range(n//2):  # there are only n//2 layers, if N is odd then the center figure doesn't move
        first = layer  # defines the beginning of the layer in python indexing, same for row and col
        last = n-1-layer  # the ending of the layer, same for row and col
        for i in range(first,last):  # i is the current position, leaving out the last. See CTTI for illustration
            offset = i - first  # how many positions away from the first. Used for arrays not starting from top of the row/col
            top = a[first][i]
            a[first][i] = a[last-offset][first]  # top = left, one pos from last becomes one pos from first
            a[last-offset][first] = a[last][last-offset]  # left = bottom
            a[last][last-offset] = a[i][last]  # bottom = right
            a[i][last] = top
    return a


testArr = [[1,2,3,6], [4,5,'a',9], [7,8,'b',10], [3,6,8,'c']]
rotateImage(testArr)


# solution by CodeSignal user anil_k22
# rotation is first flip the top and bottom and then swap diagonal values
def rotateImage(a):
    a.reverse()
    # this construct traverse through the lower left diagonal half of a square without touching the diagonal line
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a


testArr = [[1,2,3], [4,5,6], [7,8,9]]
rotateImage(testArr)


# solution by CodeSignal user lafosse
# star operator is black magic...
# the array is first reversed, then unpacked using *, and then zipped by position
# think of a zipper to imaging how zip() works - stitching up the individual elements across iterables.
def rotateImage(a):
    return list(zip(*reversed(a)))

testArr = [[1,2,3], [4,5,6], [7,8,9]]
rotateImage(testArr)


